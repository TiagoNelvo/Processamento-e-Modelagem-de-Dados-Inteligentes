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

boston_features = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','TAX','PTRATIO','B','LSTAT','MEDV']

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
#   Transformação de dados
#   Visualização de dados