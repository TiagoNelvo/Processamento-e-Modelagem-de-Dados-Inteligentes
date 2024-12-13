import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nomes_produtos = ['Camisa Manga Longa', 'Camisa Gola Polo', 'Camiseta Básica', 'Calça Jeans', 'Sapato Social']

nomes_produtos

df_loja = pd.DataFrame({'ID Produto':np.random.randint(1,11,1000),
                        'Nome Produto': np.random.choice(nomes_produtos,1000),
                        'Quantidade Vendida': np.random.randint(1,21,1000),
                        'Preco Unitario': np.round(np.random.uniform(10,100,1000),2),
                        'Data da Venda': np.random.choice(pd.date_range(start='2021-01-01', end='2021-12-31'),1000)
                        })

df_loja

df_loja.describe()

df_loja.to_csv('vendas_nova_aula.csv', index=False)



print(df_loja.loc[:'ID Produto'])
print(df_loja.loc['ID Produto':'Quantidade Vendida'])

df_loja['Nome Produto'].map(lambda x:x.upper())

#df_loja['Nome Produto'] = df_loja['Nome Produto'].map(lambda x:x.upper())

df_loja_teste = df_loja
df_loja_teste['Nome Produto'] = df_loja['Nome Produto'].map(lambda x:x.upper())
df_loja_teste
df_loja

# Sort_values organizando por ordem crescente/decrecente

df_loja.sort_values(by='Preco Unitario', ascending=False)
df_loja.sort_values(by='Preco Unitario', ascending=True)
df_loja

df_loja_crescente = df_loja.sort_values(by='Preco Unitario', ascending=False)
df_loja_crescente

# Groupby Agrupamento
df_loja.groupby('Preco Unitario').mean(numeric_only=True) # o mean não funciona com string
df_loja.groupby('Nome Produto').mean()


df_group = df_loja.groupby('Nome Produto').mean()
df_group

# Gerando o gráfico de barras com as médias de vendas por produto
plt.bar(df_group.index, df_group['Quantidade Vendida'])
plt.xticks(rotation=45)
plt.ylabel('Média de vendas')
plt.title('Média de vendas por produto')
plt.show()


