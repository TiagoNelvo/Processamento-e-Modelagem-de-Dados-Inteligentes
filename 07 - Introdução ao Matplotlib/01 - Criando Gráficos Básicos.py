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

# Criando Gráficos básicos

# Adicionando coluna Mes
df_loja['Mes'] = pd.DatetimeIndex(df_loja['Data da Venda']).month
df_loja

# Vendas Mensais
df_loja_vendas_por_mes = df_loja.groupby(['Nome Produto', 'Mes'])['Quantidade Vendida'].sum()
df_loja_vendas_por_mes

# Vendas mensais de camisa manga longa
df_loja_vendas_manga_longa = df_loja_vendas_por_mes.loc['CAMISA MANGA LONGA']
df_loja_vendas_manga_longa

# Vendas mensais de camisa gola polo
df_loja_vendas_gola_polo = df_loja_vendas_por_mes.loc['CAMISA GOLA POLO']
df_loja_vendas_gola_polo

# Vendas mensais de calça jeans
df_loja_vendas_calca_jeans = df_loja_vendas_por_mes.loc['CALÇA JEANS']
df_loja_vendas_calca_jeans

# Vendas mensais de camiseta basica
df_loja_vendas_camiseta_basica = df_loja_vendas_por_mes.loc['CAMISETA BÁSICA']
df_loja_vendas_camiseta_basica

# Vendas mensais de sapato social
df_loja_vendas_sapato_social = df_loja_vendas_por_mes.loc['SAPATO SOCIAL']
df_loja_vendas_sapato_social

# Construindo Gráfico

# Estrutura do gráfico
plt.plot(df_loja_vendas_manga_longa.index, df_loja_vendas_manga_longa.values, label = 'Camisa Manga Longa')
plt.plot(df_loja_vendas_gola_polo.index, df_loja_vendas_gola_polo.values, label = 'Camisa Gola Polo')
plt.plot(df_loja_vendas_camiseta_basica.index, df_loja_vendas_camiseta_basica.values, label = 'Camiseta Básica')
plt.plot(df_loja_vendas_calca_jeans.index, df_loja_vendas_calca_jeans.values, label = 'Calça Jeans')
plt.plot(df_loja_vendas_sapato_social.index, df_loja_vendas_sapato_social.values, label = 'Sapato Social')

# Personalização do Gráfico
plt.legend()
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
plt.ylabel('Quantidade Vendida')
plt.title('Quantidade Total Vendida de Cada Produto')
plt.show

# Fazendo em barras (trocar o plt.plot por plt.bar)
# Estrutura do gráfico
plt.bar(df_loja_vendas_manga_longa.index, df_loja_vendas_manga_longa.values, label = 'Camisa Manga Longa')
plt.bar(df_loja_vendas_gola_polo.index, df_loja_vendas_gola_polo.values, label = 'Camisa Gola Polo')
plt.bar(df_loja_vendas_camiseta_basica.index, df_loja_vendas_camiseta_basica.values, label = 'Camiseta Básica')
plt.bar(df_loja_vendas_calca_jeans.index, df_loja_vendas_calca_jeans.values, label = 'Calça Jeans')
plt.bar(df_loja_vendas_sapato_social.index, df_loja_vendas_sapato_social.values, label = 'Sapato Social')

# Personalização do Gráfico
plt.legend()
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
plt.ylabel('Quantidade Vendida')
plt.title('Quantidade Total Vendida de Cada Produto')
plt.show

# Gráfico das Médias

df_agrupados = df_loja.groupby('Nome Produto').mean()

# Gráfico
plt.bar(df_agrupados.index, df_agrupados['Quantidade Vendida'], color=['red','blue','green','orange','purple'])
plt.xticks(rotation=45)
plt.ylabel('Média de Vendas')
plt.title('Média de Vendas por Produto')
plt.grid(axis='y',linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Função dos Gráficos
def grafico_media():
    plt.figure()
    plt.bar(df_agrupados.index, df_agrupados['Quantidade Vendida'], color=['red','blue','green','orange','purple'])
    plt.xticks(rotation=45)
    plt.ylabel('Média de Vendas')
    plt.title('Média de Vendas por Produto')
    plt.grid(axis='y',linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show() 

grafico_media()

# Grafico em linha
def grafico_linha():
# Estrutura do gráfico
    plt.figure()
    plt.plot(df_loja_vendas_manga_longa.index, df_loja_vendas_manga_longa.values, label = 'Camisa Manga Longa')
    plt.plot(df_loja_vendas_gola_polo.index, df_loja_vendas_gola_polo.values, label = 'Camisa Gola Polo')
    plt.plot(df_loja_vendas_camiseta_basica.index, df_loja_vendas_camiseta_basica.values, label = 'Camiseta Básica')
    plt.plot(df_loja_vendas_calca_jeans.index, df_loja_vendas_calca_jeans.values, label = 'Calça Jeans')
    plt.plot(df_loja_vendas_sapato_social.index, df_loja_vendas_sapato_social.values, label = 'Sapato Social')

    # Personalização do Gráfico
    plt.legend()
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
    plt.ylabel('Quantidade Vendida')
    plt.title('Quantidade Total Vendida de Cada Produto')
    plt.show
    
grafico_linha()

# Função Grafico em barra
def grafico_bar():
# Estrutura do gráfico
    plt.figure()
    plt.bar(df_loja_vendas_manga_longa.index, df_loja_vendas_manga_longa.values, label = 'Camisa Manga Longa')
    plt.bar(df_loja_vendas_gola_polo.index, df_loja_vendas_gola_polo.values, label = 'Camisa Gola Polo')
    plt.bar(df_loja_vendas_camiseta_basica.index, df_loja_vendas_camiseta_basica.values, label = 'Camiseta Básica')
    plt.bar(df_loja_vendas_calca_jeans.index, df_loja_vendas_calca_jeans.values, label = 'Calça Jeans')
    plt.bar(df_loja_vendas_sapato_social.index, df_loja_vendas_sapato_social.values, label = 'Sapato Social')

    # Personalização do Gráfico
    plt.legend()
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez'])
    plt.ylabel('Quantidade Vendida')
    plt.title('Quantidade Total Vendida de Cada Produto')
    plt.show
grafico_bar()

def chamar_graficos():
    grafico_linha()
    grafico_bar()
    grafico_media()
    
chamar_graficos()

# Scatter

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(df_loja['Preco Unitario'],df_loja['Quantidade Vendida'], alpha=0.5, s=50, c='purple')
plt.xlabel('Preco Unitário', fontsize=12)
plt.ylabel('Quantidade Vendida', fontsize=12)
plt.title('Relação entre o preço unitário e a quantidade vendida',fontsize=14)
plt.grid(axis='both',linestyle='--',alpha=0.7)
plt.tight_layout()
plt.show

# Função do codigo scatter
def grafico_scatter():
    plt.figure()
    plt.scatter(df_loja['Preco Unitario'], df_loja['Quantidade Vendida'], alpha=0.5, s=50, c='red')
    plt.xlabel('Preço Unitario', fontsize=12)
    plt.ylabel('Quantidade Vendida', fontsize=12)
    plt.title('Relação entre o preco unitário e a quantidade vendida', fontsize=14)
    plt.grid(axis='both',linestyle='--',alpha=0.7) #'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
    plt.tight_layout
    plt.show()
grafico_scatter()















