import pandas as pd
import streamlit as st
import folium
import geopandas
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from numerize.numerize import numerize
from PIL import Image

## ===== Configuração da Página =====

st.set_page_config(page_title='House Rocket Insights', page_icon="🏠", layout='wide')
pd.set_option('display.float_format', lambda x: '%.2f' % x)

## ===== Cabeçalho =====

c1, c2 = st.columns((1, 1))

with c1:
    st.title('House Rocket Company')
    st.markdown('**Análise de Dados de Imóveis Disponíveis em King County, USA**')
    st.markdown(
        'Esse relatório faz parte do Projeto de Insights da *House Rocket*, uma empresa fictícia que compra e vende'
        ' imóveis através de uma plataforma digital.')
    st.markdown(
        'O relatório foi feito por **Nicolas Doege**, a pedidos do CEO, com o objetivo de analisar os imóveis disponíveis'
        ' na região de King County, Washington, USA.')
    st.markdown('Informações Adicionais: [Repositório](https://github.com/doegemon)')

with c2:
    photo = Image.open('kc.jpg')
    st.image(photo)

## ===== Funções =====

@st.cache(allow_output_mutation=True)
def get_data(file_path):
    data = pd.read_csv(file_path)
    return data


@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)
    return geofile


def convert_csv(data):
    return data.to_csv().encode('utf-8')


def data_overview(data):
    st.title('Principais Informações')
    invested = data[data['recommendation'] == 'buy']['price'].sum()
    returned = data[data['recommendation'] == 'buy']['selling_price_suggestion'].sum()
    profit = data[data['recommendation'] == 'buy']['expected_profit'].sum()

    c1, c2 = st.columns((1, 3))
    with c1:
        st.header('Dados Financeiros')
        st.metric(label='Custo Máximo do Investimento', value=numerize(invested))
        st.metric(label='Retorno Máximo do Investimento', value=numerize(returned))
        st.metric(label='Lucro Máximo Estimado', value=numerize(profit))
    with c2:
        st.header('Principais Descobertas:')
        st.write('**1. Enquanto no Inverno o número de imóveis disponíveis para compra diminui, '
                 'na Primavera o número aumenta, assim como o preço médio dos imóveis.**')
        st.write('**2. Imóveis reformados são 43% mais caros em comparação a imóveis não reformados.**')
        st.write('**3. Na média, não existe muita diferença de preço entre imóveis construídos '
                 'antes de 1960 e depois de 1960.**')
        st.write('')
        st.subheader(f'Total de Imóveis Disponíveis no Portfólio: {data.shape[0]}')
        buy_count = data[data['recommendation'] == 'buy']['price'].count()
        st.subheader(f'Total de Imóveis com Recomendação de Compra: {buy_count}')

    return None


def portfolio_map_table(data, geofile):

    st.title('Imóveis do Portfólio')

    f_decision = st.checkbox('Visualizar somente Imóveis com recomendação de Compra.')

    if f_decision:
        data = data[data['recommendation'] == 'buy']
        st.write('Temos', data.shape[0], 'imóveis sendo mostrados')

    else:
        data = data.copy()
        st.write('Temos', data.shape[0], 'imóveis sendo mostrados')

    c1, c2 = st.columns((1, 1))

    with c1:

        st.subheader('Mapa')

        hr_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()], default_zoom_start=15)

        make_cluster = MarkerCluster().add_to(hr_map)

        for index, row in data.iterrows():
            folium.Marker([row['lat'], row['long']],
                      popup='Disponível desde {0} por US$ {1}.'
                            '\nZipcode: {2}'
                            '\nID: {3}'
                      .format(row['date'], row['price'], row['zipcode'], row['id'])).add_to(make_cluster)

        df_geofile = geofile[geofile['ZIP'].isin(data['zipcode'].tolist())]
        folium.features.Choropleth(data=data, geo_data=df_geofile, columns=['zipcode', 'expected_profit'],
                               key_on='feature.properties.ZIP',
                               fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2,
                               legend_name='Expected Profit').add_to(hr_map)

        folium_static(hr_map, width=650)

    with c2:
        st.subheader('Tabela')

        if f_decision:
            data = data[data['recommendation'] == 'buy']

        else:
            data = data.copy()

        table = data[['id', 'date', 'condition', 'zipcode', 'price', 'median_price', 'recommendation',
                  'selling_price_suggestion', 'expected_profit']].copy()

        st.dataframe(table.style.set_precision(2), width=700, height=500)

        data_csv = convert_csv(data)
        st.download_button(label='Baixar a Tabela como CSV',
                       data=data_csv, file_name='portfolio.csv',
                       mime='text/csv')

    return None


def profit_attributes(data):
    st.title('Atributos dos Imóveis e Lucro Estimado')
    st.markdown('*Somente Imóveis com recomendação de Compra*')

    filtered = data[data['recommendation'] == 'buy'][['id', 'condition', 'grade', 'zipcode',
                                     'price', 'median_price', 'selling_price_suggestion',
                                     'expected_profit','yr_built', 'yr_renovated',
                                     'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'view'
                                     ]].copy()

    c1, c2, c3 = st.columns((1, 2, 2))

    with c1:
        f_bedrooms = st.selectbox('Número Máximo de Quartos',
                                  filtered['bedrooms'].sort_values(ascending=True).unique().tolist(), key='bedrooms',
                                  index=2)

        f_bathrooms = st.selectbox('Número Máximo de Banheiros',
                                   filtered['bathrooms'].sort_values(ascending=True).unique().tolist(), key='bathrooms',
                                   index=7)

    with c2:
        f_sqft_living = st.slider('Tamanho Máximo do Espaço Interno',
                                  int(filtered['sqft_living'].min()),
                                  int(filtered['sqft_living'].max() + 1),
                                  value=int(filtered['sqft_living'].max() + 1), key='living')

        f_sqft_lot = st.slider('Tamanho Máximo do Imóvel',
                                    int(filtered['sqft_lot'].min()),
                                    int(filtered['sqft_lot'].max() + 1),
                                    value=int(filtered['sqft_lot'].max() + 1), key='lot')

    with c3:
        f_yrbuilt = st.slider('Ano Mínimo de Construção do Imóvel',
                              int(filtered['yr_built'].min()),
                              int(filtered['yr_built'].max()),
                              value=int(filtered['yr_built'].min()), key='yrbuilt')

        f_grade = st.slider('Classificação Mínima do Imóvel',
                                  int(filtered['grade'].min()),
                                  int(filtered['grade'].max()),
                                  value=int(filtered['grade'].min()), key='grade')

    f_buying_price = st.slider('Preço Máximo',
                               int(filtered['price'].min()),
                               int(filtered['price'].max() + 1),
                               value=int(filtered['price'].max() + 1), key='price')

    f_filtered = filtered[(filtered['bedrooms'] <= f_bedrooms) &
            (filtered['bathrooms'] <= f_bathrooms) &
            (filtered['sqft_living'] <= f_sqft_living) &
            (filtered['sqft_lot'] <= f_sqft_lot) &
            (filtered['price'] <= f_buying_price) &
            (filtered['yr_built'] >= f_yrbuilt) &
            (filtered['grade'] >= f_grade)]

    st.dataframe(f_filtered.style.set_precision(2))
    st.write(f'**Lucro Estimado: US$ {numerize(f_filtered["expected_profit"].sum())}**')
    st.write(f'*Número de Imóveis: {f_filtered["id"].count()}*')

    data_csv = convert_csv(data)
    st.download_button(label='Baixar a Tabela como CSV',
                       data=data_csv, file_name='portfolio_attributes.csv',
                       mime='text/csv')


if __name__ == '__main__':

    path = 'kc_house_data_final.csv'
    geofile_raw = get_geofile('https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson')

    df = get_data(path)
    data_overview(df)
    portfolio_map_table(df, geofile_raw)
    profit_attributes(df)
