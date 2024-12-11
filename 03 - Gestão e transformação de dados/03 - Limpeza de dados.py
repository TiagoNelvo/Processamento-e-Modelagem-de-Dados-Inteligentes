# Geração de Dados

import pandas as pd
import random

produtos = {'Arroz': 10.0, 'Feijão': 8.0, 'Óleo': 12.0, 'Açúcar': 5.0}
produtos

dados_vendas = {'Nome Produto': [], 'Quantidade Vendida':[], 'Valor Total Vendas':[]}

for produto, preco in produtos.items():
    qtd_vendida = random.randint(50,100)
    
    valor_total = qtd_vendida * preco
    
    dados_vendas['Nome Produto'].append(produto)
    dados_vendas['Quantidade Vendida'].append(qtd_vendida)
    dados_vendas['Valor Total Vendas'].append(valor_total)

df_vendas = pd.DataFrame(dados_vendas)
df_vendas
df_vendas.to_csv('vendas_descomplica.csv', index=False)