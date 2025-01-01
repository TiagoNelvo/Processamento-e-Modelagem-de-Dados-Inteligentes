#   Projeto Previsão de Valor de Aluguel em Boston
#   Apresentação do Projeto

#Features = Colunas
#Entrada de dados = Linhas


# Brainstorm e extração de dados

#Planejamento do projeto
#Objetivos do cliente
# Relação das Features

# CRIM - per capita crime rate by town

# ZN - proportion of residential land zoned for lots over 25,000 sq.ft.

# INDUS - proportion of non-retail business acres per town.

# CHAS - Charles River dummy variable (1 if tract bounds river; 0 otherwise)

# NOX - nitric oxides concentration (parts per 10 million)

# RM - average number of rooms per dwelling

# AGE - proportion of owner-occupied units built prior to 1940

# DIS - weighted distances to five Boston employment centres

# RAD - index of accessibility to radial highways

# TAX - full-value property-tax rate per $10,000

# PTRATIO - pupil-teacher ratio by town

# B - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town

# LSTAT - percent lower status of the population

# MEDV - Median value of owner-occupied homes in $1000's


#   Gestão de dados com Pandas

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import urllib.request

# Manual dos Dados:
# https://lib.stat.cmu.edu/datasets/boston

# Definindo as Features
boston_features = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']

boston_features

# dados_url = "https://archive.ics.uci.edu/ml/machine-learning-database/housing/housing.data"
# dados_url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
# local_file_path, headers = urllib.request.urlretrieve(dados_url)

# boston = pd.read_csv(local_file_path,delimiter=r"\s+",names=boston_features)
# boston = pd.read_csv("dados_aluguel_boston.data",delimiter=",",names=boston_features,skiprows=1)
boston = pd.read_csv("dados_aluguel_boston.csv",delimiter=",",names=boston_features,skiprows=1)
boston

boston.describe()
boston.corr()
boston.head()
boston.tail()
boston.iloc[:,:-1] # Iloc para filtrar os dados do X / #[:,:-1] vai retirar a ultima coluna
boston.iloc[:-1] # Iloc para filtrar os dados do y vai exibir apenas a ultima coluna


X = boston.iloc[:,:-1] # dados para o treinamento 
y = boston.iloc[:,-1] # dados para o treinamento y (métrica que eu quero prever)

#Divisão dos dados de treinamento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

modelo_gb = GradientBoostingRegressor()

modelo_gb.fit(X_train, y_train)

score = modelo_gb.score(X_test,y_test)
print('Acurácia do modelo: ', score)


#   Apresentação do Projeto de ML


# Previsão

# CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT	MEDV

dados_entrada = [0.1,20,6,0,0.4,6,60,4,400,18,350,12,5]
previsao = modelo_gb.predict([dados_entrada])

# Visualização da previsão:
print('Preço estimado para a casa: ',previsao[0])


# Coleta de dados para Data Storytelling

import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

mascara = np.zeros_like(boston.corr())
triangle_indices = np.triu_indices_from(mascara)
mascara[triangle_indices] = True

def grafico_heatmap():
    
    
    plt.figure(figsize=(16,10))
    sns.heatmap(boston.corr(),annot=True,annot_kws={"size":14})
    sns.set_style('white')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()
    
    plt.figure(figsize=(16,10))
    sns.heatmap(boston.corr(), mask=mascara,annot=True,annot_kws={"size":14})
    sns.set_style('white')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()
    
grafico_heatmap()

def grafico_joinplot():
    plt.figure()
    sns.set()
    sns.set_context('talk')
    sns.set_style('whitegrid')
    sns.jointplot(x=boston['DIS'], y=boston['NOX'], size=7, color='indigo',joint_kws={'alpha':0.5})
    plt.show()

grafico_joinplot()

def grafico_joinplot_tax_rad():
    plt.figure()
    sns.set()
    sns.set_context('talk')
    sns.set_style('whitegrid')
    sns.jointplot(x=boston['TAX'], y=boston['RAD'], height=7, color='darkred', joint_kws={'alpha':0.5} )
    plt.show()

grafico_joinplot_tax_rad()

def grafico_hex():
    plt.figure()
    sns.set()
    sns.set_context('talk')
    sns.set_style('whitegrid')
    sns.jointplot(x=boston['DIS'], y=boston['NOX'], kind='hex',height=7, color='blue')
    plt.show()

grafico_hex()

def grafico_prof_valor():
    plt.figure()
    sns.set()
    sns.set_context('talk')
    sns.set_style('whitegrid')
    sns.jointplot(x=boston['PTRATIO'], y=boston['MEDV'], kind='hex', height=7,color='blue')
    plt.show()
    
grafico_prof_valor()

def chamar_graficos():
    grafico_heatmap()
    grafico_joinplot()
    grafico_joinplot_tax()
    grafico_hex()
    grafico_prof_valor()

    
chamar_graficos()

def graficos_correlacao():
    plt.figure()
    sns.lmplot(x='TAX',y='RAD', data=boston, height=7)
    plt.show()
    
    plt.figure()
    sns.lmplot(x='MEDV',y='RAD', data=boston, height=7)
    plt.show()
    
    plt.figure()
    sns.lmplot(x='PTRATIO',y='MEDV', data=boston, height=7)
    plt.show()

graficos_correlacao()

boston_filtro_menor_45 = boston.loc[boston['MEDV'] < 45]

boston_filtro_maior_10

boston

boston_filtro_maior_45

boston_filtro_menor_45

sns.lmplot(x='PTRATIO',y='MEDV', data=boston_filtro_menor_45, height=7)
plt.show()

filtro = boston.loc[(boston['MEDV'] > 45) & (boston['PTRATIO'] > 14)]

filtro

sns.lmplot(x='PTRATIO',y='MEDV', data=filtro, height=7)
plt.show()

rm_medv_corr = round(boston['RM'].corr(boston['MEDV']),3)

rm_medv_corr

plt.figure(figsize=(9,6))
plt.scatter(x=boston['RM'], y=boston['MEDV'], alpha=0.6, s=80, color='skyblue')

plt.title(f'N de Quartos vs PREÇO (Correlação {rm_medv_corr})',fontsize=14)
plt.xlabel('RM - Mediano de Quartos',fontsize=14)
plt.ylabel('PREÇO - Preço da propriedade em milhares de dólares',fontsize=14)



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







