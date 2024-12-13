from op_ma import *

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





