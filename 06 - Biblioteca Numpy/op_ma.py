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


