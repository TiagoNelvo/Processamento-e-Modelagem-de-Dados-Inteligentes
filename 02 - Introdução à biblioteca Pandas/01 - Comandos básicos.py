import pandas as pd

arquivo_serie = pd.Series([1,3,5,7,9])
print(arquivo_serie)
print('------------')

# Criando um DataFrame

dados = {'nome':['João', 'Maria', 'José', 'Ana', 'Pedro'],
         'idade':[20,25,30,35,40],
         'cidade':['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']}

df_descomplica = pd.DataFrame(dados)
print(df_descomplica)