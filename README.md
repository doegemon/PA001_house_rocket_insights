# PA001_House_Rocket_Insights
Os objetivos desse projeto de Ciência de Dados são: 

- Realizar a Análise Exploratória de Dados (EDA) dos imóveis disponíveis em King County, Washington, EUA, através do conjunto de dados fornecido; 
- Indicar quais imóveis devem ser comprados pela empresa fictícia House Rocket de acordo com os critérios estabelecidos pelo CEO; e
- Elaborar um relatório/dashboard que possa ser acessado por qualquer um da empresa.

# 01. Problema de Negócio
O modelo de negócio da companhia fictícia House Rocket é comprar e vender imóveis através de uma plataforma digital. Como Analista de Dados da companhia, fui encarregado de elaborar um relatório/dashboard para que o CEO e demais tomadores de decisão da empresa possam visualizar os imóveis disponíveis em King County, com o objetivo de expandir o portfólio da companhia. 

Os objetivos principais do relatório/dashboard são: 
- Mostrar os imóveis disponíveis na região;
- Indicar quais imóveis devem ser comprados; e
- Os resultados financeiros envolvidos na operação.

# 02. Resultados Financeiros
Após a devida limpeza dos dados, restaram 21.421 imóveis no conjunto de dados.

Com a aplicação dos critérios estabelecidos pelo CEO, foi recomendada a compra de 10.635 imóveis.

Traduzindo em dados financeiros: 
- Custo Máximo do Investimento: US$ 4.14B
- Retorno Máximo do Investimento: US$ 5.38B
- Lucro Máximo Estimado: US$ 1.24B
- Margem Bruta: 30.0%

# 03. Premissas de Negócio
- O conjunto de dados contém imóveis disponíveis para venda entre maio de 2014 e maio de 2015;
- Alguns imóveis com o número de quartos incompatível com o tamanho interno do imóvel foram removidos, vez que provavelmente foi um erro de digitação; 
- Estações: 
  - Primavera começa em 21 de março; 
  - Verão começa em 21 de junho; 
  - Outono começa em 23 de setembro; e
  - Inverno começa em 21 de dezembro.
- Critérios estabelecidos pelo CEO para a compra de imóveis: 
  - Imóvel deve ter uma condição/conservação igual ou maior que 3; e
  - O preço do imóvel deve estar igual ou abaixo do preço mediano da região (*zipcode* ou caixa-postal).
- As variáveis/atributos (originais e criadas para a análise) do conjunto de dados são: 

|    Atributos    |                         Significado                          |
| :-------------: | :----------------------------------------------------------: |
|       id        |Identificador único de cada imóvel                            |
|      date       |Data de anúncio do imóvel                                     |
|      price      |Preço de venda do imóvel                                      |
|    bedrooms     |Número de quartos                                             |
|    bathrooms    |Número de banheiros (.5 significa um banheiro com privada mas sem chuveiro, enquanto .75 ou 3/4 significa um banheiro com uma torneira, uma privada e um chuveiro ou banheira)                                                       |
|   sqft_living   |Espaço interno do imóvel em pés quadrados                    |
|    sqft_lot     |Tamanho do terreno imóvel em pés quadrados               |
|     floors      |Número de andares do imóvel                  |
|   waterfront    |Se o imóvel tem frente para a água/lago ou não               |
|      view       |Um índice de 0 a 4 representando a qualidade da vista do imóvel |
|    condition    |Um índice de 1 a 5 representando o estado de conservação do imóvel |
|      grade      |Um índice de 1 a 13 representando a qualidade da construção e design do imóvel |
|  sqft_above     |Tamanho do espaço interno do imóvel acima do nível da superfície em pés quadrados |
|  sqft_basement  |Tamanho do espaço interno do imóvel abaixo do nível da superfície em pés quadrados | |
|    yr_built     |Ano de construção do imóvel                    |
|  yr_renovated   |Ano de reforma do imóvel                      |
|     zipcode     |Código postal da região do imóvel     |
|       lat       |Latitude                           |
|      long       |Longitude                           |
| sqft_livining15 |Tamanho do espaço interno do imóvel em pés quadrados para os 15 vizinhos mais próximos |
|   sqft_lot15    |Tamanho do terreno do imóvel em pés quadrados para os 15 vizinhos mais próximos |
|      median_price      |Preço mediano da região (zipcode) onde o imóvel se encontra    |
|      recommendation      |Recomendação de comprar ou não comprar o imóvel     |
|      selling_price_suggestion      |Se a recomendação for comprar de comprar o imóvel, sugestão de preço de venda (acréscimo de 30% sobre o valor de compra) |
|      expected_profit      |Lucro esperado com a compra e venda do imóvel pelo preço sugerido |
|      season          |Estação do ano que o imóvel foi anunciado |
|      med_autumn      |Preço mediano no Outono da região (zipcode) onde o imóvel se encontra |
|      med_spring      |Preço mediano na Primavera da região (zipcode) onde o imóvel se encontra |
|      med_summer      |Preço mediano no Verão da região (zipcode) onde o imóvel se encontra |
|      med_winter      |Preço mediano no Inverno da região (zipcode) onde o imóvel se encontra |
|      best_season_to_buy      | Melhor estação do ano para comprar o imóvel (considerando o preço mediano da região) |
|      best_season_to_sell     | Melhor estação do ano para vender o imóvel (considerando o preço mediano da região)  |

# 04. Etapas do Projeto
1. Entender o modelo de negócio da companhia; 
2. Entender o problema de negócio apresentado pelo CEO; 
3. Coletar os dados; 
4. Limpeza e filtragem dos dados; 
5. Análise Exploratória de Dados; 
6. Levantamento e validação de hipóteses; 
7. Publicação do dashboard/relatório no Streamlit. 

# 05. Hipóteses de Negócio
Entre as 10 hipóteses de negócio levantadas e analisadas, as 03 principais foram: 
1. Enquanto no Inverno o número de imóveis disponíveis para compra diminui, na Primavera o número aumenta, assim como o preço médio dos imóveis; 
2. móveis reformados são 43% mais caros em comparação a imóveis não reformados; e
3. Na média, não existe muita diferença de preço entre imóveis construídos antes de 1960 e depois de 1960.

# 06. Conclusões
Feita a Análise Exploratória dos Dados e respondida as perguntas de negócio feitas pelo CEO, a publicação do relatório/dashboard no Streamlit permite que o CEO e outros tomadores de decisão acessar o arquivo de qualquer lugar, facilitando a visualização do portfólio de imóveis e a tomada de decisões de negócio. 

Ainda, as hipóteses levantadas e validadas também trazem informações importantes para a tomada de decisões e forma de condução de negócios. 

# 07. Próximos Passos
- Expandir esse método de análise de dados para outras regiões que a companhia já tem presença ou deseja expandir; 
- O método pode ser melhorado com a utilização de modelos de regressão para determinar se o imóvel está sendo anunciado por um bom preço, bem como por qual preço ele pode ser vendido; 
- Ainda, poderia ser feita uma pesquisa de mercado para coletar dados acerca dos clientes, para posterior utilização de um algoritmo de clusterização para identificar quais atributos dos imóveis cada grupo de clientes prefere. 

# Referências
- Conjunto de Dados: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
- Discussão acerca do conjunto de dados: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction/discussion/207885
