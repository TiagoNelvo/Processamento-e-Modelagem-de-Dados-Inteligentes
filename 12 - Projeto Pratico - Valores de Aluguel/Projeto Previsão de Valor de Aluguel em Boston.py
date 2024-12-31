#   Projeto Previsão de Valor de Aluguel em Boston
#   Apresentação do Projeto

#Features = Colunas
#Entrada de dados = Linhas


# Brainstorm e extração de dados

#Planejamento do projeto
#Objetivos do cliente
#Relação das Features


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

#dados_url = "https://archive.ics.uci.edu/ml/machine-learning-database/housing/housing.data"
dados_url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
local_file_path, headers = urllib.request.urlretrieve(dados_url)

boston = pd.read_csv(local_file_path,delimiter=r"\s+",names=boston_features)
with open('dados_vendas.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(local_file_path)
dados = local_file_path, headers = urllib.request.urlretrieve(dados_url)

dados.to_csv('dados_vendas.csv', index=False)
boston



#df_boston = pd.DataFrame


#   Transformação de dados
#   Visualização de dados