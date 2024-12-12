# Otimização de Recursos

import pandas as pd

base_padrao = {'Nome': ['Alice', 'Alan', 'Carol', 'Anelise', 'Evelin', 'Davi'],
                'Genero': ['F', 'M', 'F', 'F', 'F', 'NB'],
                'Salario': [10000,10000,10000,10000,10000,10000],
                'Idade': [20,21,29,22,19,18],
                'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Campinas', 'Maceio', 'Brasilia']                
                }

base_padrao

# DataFrame

df_padrao = pd.DataFrame(base_padrao)
df_padrao

# Iteração em conjuntos de dados

df_teste = df_padrao
df_teste

for index, row in df_teste.iterrows():
    if row['Cidade'] == 'São Paulo': 
        df_teste.at[index, 'Idade'] = 77
        
df_teste

# Agrupamento de pessoas por idade

for index, row in df_teste.iterrows():
    if row['Idade'] < 30:
        df_teste.at[index,'Grupo_Idade'] = 'Jovem'
    else:
        df_teste.at[index, 'Grupo_Idade'] = 'Experiente'
    
df_teste
