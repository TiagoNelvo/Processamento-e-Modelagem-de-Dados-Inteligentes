

#   Análise Exploratória

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# https://raw.githubusercontent.com/alanddantas/data/main/diamantes_manual.csv

df_diamantes = pd.read_csv('diamantes.csv')

url = "LINK QUE ESTÁ NO MATERIAL DE APOIO"
df_diamantes_url = pd.read(url)

df_diamantes

print(df_diamantes.shape)

print(df_diamantes.head())

print(df_diamantes.tail())

df_diamantes.describe()

df_diamantes.describe()

df_diamantes.corr()

df_diamantes_agrupado = df_diamantes.groupby('carat').agg(['mean','median','min','max'])

df_diamantes.sample(3)

df_diamantes.dtypes

df_diamantes.columns

df_diamantes.nunique()

df_diamantes.isnull().sum()

df_diamantes.info()

#   Treinamento do Modelo

X = df_diamantes[['carat','depth','table','x','y','z']]
y = df_diamantes['price']

X_train,X_test,y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

modelo_reg = LinearRegression()
modelo_reg.fit(X_train, y_train)
y_pred = modelo_reg.predict(X_test)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test, y_pred)

print('Avaliação do Modelo:')
print(f'MSE: {mse:.2f}')
print(f'R2: {r2:.2f}'

novos_diamantes = pd.DataFrame({
    'carat':[0.9,1.2,2.3],
    'depth':[62.1,60.5,63.2],
    'table':[57,63,61],
    'x':[5.1,6.78,8.3],
    'y':[5.15,6.82,8.35],
    'z':[3.18,4.1,5.12]
})

novos_diamantes

precos_novos_diamantes = modelo_reg.predict(novos_diamantes)

print('O preço previso para os 3 diamantes é:', precos_novos_diamantes)
contador = 1 #count

for preco in precos_novos_diamantes:
    print(f'O preço previso para o diamante {contador} é',preco)
    contador = contador + 1

#   Modelagem de Dados

# Metodologia

# ETL (Extração, transformação e carregamento de dados)

# Análise de Requisitos;
# Design conceitual;
# Desenho Lógico;
# Implementação.
# Neste projeto prático, vamos criar um modelo de dados para uma loja virtual, considerando os seguintes requisitos:

# A loja vende produtos de diferentes categorias, como eletrônicos, roupas, acessórios, etc.

# Cada produto tem um nome, uma descrição, um preço, uma imagem e uma categoria.

# Cada categoria tem um nome e uma descrição.

# Os clientes da loja podem criar uma conta para fazer compras, e cada conta tem um nome, um endereço de e-mail e uma senha.

# Os clientes podem adicionar produtos ao carrinho de compras e finalizar a compra.

# Cada compra tem um número de identificação, uma data e uma lista de produtos comprados.

# Para cada produto comprado, registra-se a quantidade e o preço unitário na data da compra.

# Com base nesses requisitos, podemos criar um modelo de dados com as seguintes tabelas:

# Produtos: ID, nome, descrição, preço, imagem, ID_categoria Categorias: ID, nome, descrição Clientes: ID, nome, e-mail, senha Compras: ID, data, ID_cliente Produtos_comprados: ID_compra, ID_produto, quantidade, preço_unitário


Produtos: ID, nome, descrição, preço, imagem, ID_categoria
Categorias: ID, nome, descrição
Clientes: ID, nome, e-mail, senha
Compras: ID, data, ID_cliente
Produtos_comprados: ID_compra, ID_produto, quantidade, preço_unitário


CREATE TABLE Clientes (
ID INT PRIMARY KEY,
nome VARCHAR(255),
email VARCHAR(255),
senha VARCHAR(50)
);

CREATE TABLE Compras (
ID INT PRIMARY KEY,
data DATE,
ID_cliente INT,
FOREIGN KEY (ID_cliente) REFERENCES Clientes(ID)
);

CREATE TABLE Produtos_comprados (
ID_compra INT,
ID_produto INT,
quantidade INT,
preco_unitario DECIMAL(10, 2),
FOREIGN KEY (ID_compra) REFERENCES Compras(ID),
FOREIGN KEY (ID_produto) REFERENCES Produtos(ID)
);

# Query 

import pandas as pd
import numpy as np

# Gerando dados

np.random.seed(42)
dados = pd.DataFrame({
    'data_venda': pd.date_range('2022-01-01',periods=365),
    'vendedor': np.random.choice(['Maria','Pedro','Alan'],size=365),
    'produto':np.random.choice(['Camisa','Calça','Tênis','Boné'],size=365),
    'preco':np.random.normal(loc=100,scale=20,size=365),
    'quantidade':np.random.randint(1,10,size=365)
    
})

dados.describe()

df_vendas = dados

df_vendas

df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'],format='%d-%m-%Y')

print(df_vendas.isnull().sum())

vendas_mes = df_vendas.groupby(pd.Grouper(key='data_venda',freq='M')).sum()['preco']

vendas_mes







