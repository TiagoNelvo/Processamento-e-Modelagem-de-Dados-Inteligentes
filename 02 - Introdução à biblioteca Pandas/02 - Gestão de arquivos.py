import pandas as pd
# Criando um DataFrame

dados = {'nome':['João', 'Maria', 'José', 'Ana', 'Pedro'],
         'idade':[20,25,30,35,40],
         'cidade':['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']}

df_descomplica = pd.DataFrame(dados)
print(df_descomplica)

# Pesquisando no Dataframe

df_descomplica['idade']

df_descomplica['cidade']

df_descomplica['idade'] = df_descomplica['idade'] + 1

df_descomplica['cidade'].str.upper()
 
# Desafio

df_descomplica['idade'] = df_descomplica['idade'] * 2

# Função Lambda

df_descomplica['idade'] = df_descomplica['idade'].apply(lambda x:x *2)

df_descomplica.at[2, 'cidade']
df_descomplica.at[2, 'cidade'] =  'Recife'