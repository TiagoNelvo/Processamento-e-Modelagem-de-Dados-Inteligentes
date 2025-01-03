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
    grafico_joinplot_tax_rad()
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

boston_filtro_maior_10 = boston.loc[boston['MEDV'] > 10]

boston_filtro_menor_45 = boston.loc[boston['MEDV'] < 45]

boston_filtro_maior_45 = boston.loc[boston['MEDV'] > 45]

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

