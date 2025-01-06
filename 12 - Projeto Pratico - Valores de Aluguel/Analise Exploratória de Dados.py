

#   Análise Exploratória

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# https://raw.githubusercontent.com/alanddantas/data/main/diamantes_manual.csv

df_diamantes = pd.read_csv('diamantes.csv')

# url = "https://github.com/alanddantas/data/blob/main/diamantes.csv"
# df_diamantes_url = pd.read(url)

df_diamantes

print(df_diamantes.shape)

print(df_diamantes.head())

print(df_diamantes.tail())

df_diamantes.describe()

df_diamantes.describe()

df_diamantes.corr()

#df_diamantes_agrupado = df_diamantes.groupby('carat').agg(['mean','median','min','max'])

df_diamantes.sample(3)

df_diamantes.dtypes

df_diamantes.columns

df_diamantes.nunique()

df_diamantes.isnull().sum()

df_diamantes.info()

#   Treinamento do Modelo

X = df_diamantes[['carat','depth','table','x','y','z']]
y = df_diamantes['price']

X_train,X_test,y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

modelo_reg = LinearRegression()
modelo_reg.fit(X_train, y_train)
y_pred = modelo_reg.predict(X_test)
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test, y_pred)

print('Avaliação do Modelo:')
print(f'MSE: {mse:.2f}')
print(f'R2: {r2:.2f}')

novos_diamantes = pd.DataFrame({
    'carat':[0.9,1.2,2.3],
    'depth':[62.1,60.5,63.2],
    'table':[57,63,61],
    'x':[5.1,6.78,8.3],
    'y':[5.15,6.82,8.35],
    'z':[3.18,4.1,5.12]
})

novos_diamantes

precos_novos_diamantes = modelo_reg.predict(novos_diamantes)

print('O preço previso para os 3 diamantes é:', precos_novos_diamantes)
contador = 1 #count

for preco in precos_novos_diamantes:
    print(f'O preço previso para o diamante {contador} é',preco)
    contador = contador + 1
