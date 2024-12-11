import pandas as pd
import random
# Projeto Cadastro de Pessoas

dados_cadastro = {'nome':['João', 'Maria', 'José','Ana', 'Pedro', 'Alan', 'Carol','Evelyn', 'Laura'],
                  'idade':[20,25,30,35,40,30,24,38,22],
                  'cidade':['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba','Campinas', 'Porto Alegre', 'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro'],
                  'sexo': ['M','F','X','X','X','X','X','X','X']
                  }
df_cadastro = pd.DataFrame(dados_cadastro)
df_cadastro


df_cadastro['sexo'].replace('X', pd.NA,inplace=True)
df_cadastro['sexo']

df_cadastro.dropna(inplace=True)
df_cadastro
