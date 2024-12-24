import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from graficos_basicos import *

df_loja['Mes'] = pd.DatetimeIndex(df_loja['Data da Venda']).month
df_loja_vendas_por_mes = df_loja.groupby(['Nome Produto','Mes'])['Quantidade Vendida'].sum()
df_agrupados = df_loja_vendas_por_mes.unstack()
df_agrupados.plot(figsize=(5,3), kind='line', marker='o')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.ylabel('Quantidade Vendida')
plt.title('Quantidade total vendida de cada produto por mês')
plt.show()

def grafico_venda_produto_mes():
    plt.figure()
    df_loja['Mes'] = pd.DatetimeIndex(df_loja['Data da Venda']).month
    df_loja_vendas_por_mes = df_loja.groupby(['Nome Produto', 'Mes'])['Quantidade Vendida'].sum()
    df_agrupados = df_loja_vendas_por_mes.unstack()
    df_agrupados.plot(figsize=(5,3), kind='line', marker='o')
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
    plt.ylabel('Quantidade Vendida')
    plt.title('Quantidade total vendida de cada produto por mês')
    plt.show()
    
grafico_venda_produto_mes()

# Grafico Pizza

df_loja_vendas_por_produto = df_loja.groupby('Nome Produto')['Quantidade Vendida'].sum()
df_loja_vendas_por_produto.plot(kind='pie', autopct='%1.1f%%')
plt.title('Quantidade total vendida por produto')
plt.show()

def grafico_pizza():
    plt.figure()
    df_loja_vendas_por_produto = df_loja.groupby('Nome Produto')['Quantidade Vendida'].sum()
    df_loja_vendas_por_produto.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Quantidade total vendida por produto')
    plt.show()
    
grafico_pizza()


# Scatter

plt.figure(figsize=(10,7))
plt.scatter(df_loja['Preco Unitario'],df_loja['Quantidade Vendida'], s=df_loja['Quantidade Vendida'] * 5, 
            c=df_loja['Preco Unitario'], cmap='plasma')
plt.xlabel('Preço Unitário')
plt.ylabel('Quantidade Vendida')
plt.title('Relação entre o preço unitário e a quantidade vendida')
plt.colorbar(label='Preço Unitário')
plt.show()

def grafico_scatter():
    plt.figure(figsize=(10,7))
    plt.scatter(df_loja['Preco Unitario'],df_loja['Quantidade Vendida'],s=df_loja['Quantidade Vendida'] * 5,
                c=df_loja['Preco Unitario'], cmap='plasma')
    plt.xlabel('Preço Unitário')
    plt.ylabel('Quantidade Vendida')
    plt.title('Relação entre o preço unitário e a quantidade vendida')
    plt.colorbar(label='Preço Unitário')
    plt.show()
    
grafico_scatter()

df_agrupamento_emplilhado = df_loja.groupby('Nome Produto').mean()
df_agrupamento_emplilhado

# DataFrames dos Produtos
print(df_loja_vendas_manga_longa)
print(df_loja_vendas_gola_polo)
print(df_loja_vendas_camiseta_basica)
print(df_loja_vendas_calca_jeans)
print(df_loja_vendas_sapato_social)

# Grafico barra compação

df_grouped = df_loja.groupby('Nome Produto').mean()
labels = df_grouped.index
camisa_manga_longa = df_grouped.loc['CAMISA MANGA LONGA', 'Quantidade Vendida']
camisa_gola_polo = df_grouped.loc['CAMISA GOLA POLO', 'Quantidade Vendida']
camiseta_basica = df_grouped.loc['CAMISETA BÁSICA', 'Quantidade Vendida']
calca_jeans = df_grouped.loc['CALÇA JEANS', 'Quantidade Vendida']
sapato_social = df_grouped.loc['SAPATO SOCIAL', 'Quantidade Vendida']

fig, ax =plt.subplots()
ax.bar(labels, camisa_manga_longa, label='Camisa Manga Longa', color='b')
ax.bar(labels, camisa_gola_polo, label='Camisa Gola Polo', color='g')
ax.bar(labels, camiseta_basica, label='Camiseta Básica', bottom=camisa_manga_longa+camisa_gola_polo, color='r')
ax.bar(labels, calca_jeans, label='Calça Jeans',bottom=camisa_manga_longa+camisa_gola_polo+camiseta_basica, color='c')
ax.bar(labels, sapato_social, label='Sapato Social', bottom=camisa_manga_longa+camisa_gola_polo+camiseta_basica+calca_jeans+sapato_social, color='purple')
ax.set_ylabel('Quantidade Vendida')
ax.set_xlabel('Nome do Produto')
ax.set_title('Vendas por Produto')
ax.legend()
plt.show()

def grafico_bar_comp():
        
    plt.figure()
    labels = df_grouped.index
    camisa_manga_longa = df_grouped.loc['CAMISA MANGA LONGA', 'Quantidade Vendida']
    camisa_gola_polo = df_grouped.loc['CAMISA GOLA POLO', 'Quantidade Vendida']
    camiseta_basica = df_grouped.loc['CAMISETA BÁSICA', 'Quantidade Vendida']
    calca_jeans = df_grouped.loc['CALÇA JEANS', 'Quantidade Vendida']
    sapato_social = df_grouped.loc['SAPATO SOCIAL', 'Quantidade Vendida']

    fig, ax =plt.subplots()
    ax.bar(labels, camisa_manga_longa, label='Camisa Manga Longa', color='b')
    ax.bar(labels, camisa_gola_polo, label='Camisa Gola Polo', color='g')
    ax.bar(labels, camiseta_basica, label='Camiseta Básica', bottom=camisa_manga_longa+camisa_gola_polo, color='r')
    ax.bar(labels, calca_jeans, label='Calça Jeans',bottom=camisa_manga_longa+camisa_gola_polo+camiseta_basica, color='c')
    ax.bar(labels, sapato_social, label='Sapato Social', bottom=camisa_manga_longa+camisa_gola_polo+camiseta_basica+calca_jeans+sapato_social, color='purple')
    ax.set_ylabel('Quantidade Vendida')
    ax.set_xlabel('Nome do Produto')
    ax.set_title('Vendas por Produto')
    ax.legend()
    plt.show()

grafico_bar_comp()

# Gráfico 3D

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x = df_loja['ID Produto']
y = df_loja['Quantidade Vendida']
z = df_loja['Preco Unitario']

ax.scatter(x,y,z)

ax.set_xlabel('ID Produto')
ax.set_ylabel('Quantidade Vendida')
ax.set_zlabel('Preço Unitário')

plt.show()

def grafico_3d():
        
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    x = df_loja['ID Produto']
    y = df_loja['Quantidade Vendida']
    z = df_loja['Preco Unitario']

    ax.scatter(x,y,z)

    ax.set_xlabel('ID Produto')
    ax.set_ylabel('Quantidade Vendida')
    ax.set_zlabel('Preço Unitário')

    plt.show()

grafico_3d()

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111,projection='3d')

x = df_loja['ID Produto']
y = df_loja['Quantidade Vendida']
z = df_loja['Preco Unitario']

ax.scatter(x,y,z,c=z,cmap='coolwarm', s=y*10)

ax.set_xlabel('Id Produto', fontsize=12)
ax.set_ylabel('Quantidade Vendida', fontsize=12)
ax.set_zlabel('Preço Unitário', fontsize=12)

ax.tick_params(axis='both',labelsize=10)

ax.set_xlim(0,11)
ax.set_ylim(0,23)
ax.set_zlim(10,110)

plt.title('Relação entre o preço unitário, a Quantidade vendida e o Id do produto', fontsize=16)
plt.show()

def grafico_3d_cor():
        
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111,projection='3d')

    x = df_loja['ID Produto']
    y = df_loja['Quantidade Vendida']
    z = df_loja['Preco Unitario']

    ax.scatter(x,y,z,c=z,cmap='coolwarm', s=y*10)

    ax.set_xlabel('Id Produto', fontsize=12)
    ax.set_ylabel('Quantidade Vendida', fontsize=12)
    ax.set_zlabel('Preço Unitário', fontsize=12)

    ax.tick_params(axis='both',labelsize=10)

    ax.set_xlim(0,11)
    ax.set_ylim(0,23)
    ax.set_zlim(10,110)

    plt.title('Relação entre o preço unitário, a Quantidade vendida e o Id do produto', fontsize=16)
    plt.show()

grafico_3d_cor()


def chamar_graficos_1():
    grafico_venda_produto_mes()
    grafico_pizza()
    grafico_scatter()
    grafico_bar_comp()
    grafico_3d()
    grafico_3d_cor()
    
    
    
chamar_graficos_1()








