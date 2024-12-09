import pandas as pd

# Criando um novo dataframe

dados_frutas = {'fruta':['maçã', 'banana', 'laranja', 'uva'],
                'preço':['1.50', '0.50', '2.20', '0.75'],
                'quantidade':[100, 200, 50, 75]}

dados_frutas
df_frutas = pd.DataFrame(dados_frutas)
df_frutas
print(df_frutas)

selecao = ['fruta', 'quantidade']
selecao
df_frutas['fruta'], ['quantidade']
selecao = df_frutas['fruta'], ['quantidade']
selecao