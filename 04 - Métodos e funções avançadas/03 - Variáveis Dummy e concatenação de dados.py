# Variaveis Dummy e concatenação

import pandas as pd

dados_1 = {'Nome': ['Alice', 'Alan', 'Carol', 'Anelise', 'Evelin', 'Davi'],
           'Idade': [30,85,40,20,70,75]                
                }


dados_2 = {'Nome': ['João', 'Maria', 'José', 'Marcelo', 'Berenice', 'Claudio'],
           'Idade': [10,25,70,30,74,45]              
                }

# DataFrame
df1 = pd.DataFrame(dados_1)
df1
df2 = pd.DataFrame(dados_2)
df2

df_concatenado = pd.concat([df1,df2],axis=0)

df_concatenado

# Variaveis Dummy


dados_dummy = {'Nome': ['Alice', 'Alan', 'Carol', 'Anelise', 'Evelin', 'Davi'],
           'Genero': ['F', 'M', 'F', 'F', 'F', 'NB']                
                }

dados_dummy

df_dummy = pd.DataFrame(dados_dummy)
df_dummy

df_dummy['GostaPerfume'] = df_dummy['Genero'].replace({'F':1, 'M':0, 'NB':0}).astype(int)
df_dummy