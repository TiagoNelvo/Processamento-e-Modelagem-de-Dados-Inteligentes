# Algoritmos e redes neurais

# Random Forest

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

num_alunos = 1000
faixa_idade = (16,30)
faixa_nota = (2.0,4.0)
faixa_horas_estudo = (1,20)
areas_formacao = ['Ciência da Computação','Engrenharia','Matemática','Física']

alunos = []
for i in range(num_alunos):
    idade = np.random.randint(faixa_idade[0],faixa_idade[1]+1)
    nota = np.random.uniform(faixa_nota[0], faixa_nota[1])
    horas_estudo = np.random.randint(faixa_horas_estudo[0],faixa_horas_estudo[1]+1)
    area_formacao = np.random.choice(areas_formacao)
    alunos.append({'idade':idade,'nota':nota,'horas_estudo':horas_estudo,'area_formacao':areas_formacao})


df_alunos = pd.DataFrame(alunos)

df_alunos

df_alunos.to_csv('dados_alunos.csv',index=False)

df_alunos['desempenho'] = ['alto' if x >= 70 else 'baixo' for x in df_alunos['nota']]

df_alunos

# Treinamento

X = df_alunos[['idade','nota','horas_estudo']]
y = df_alunos['desempenho']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2, random_state=42)

modelo_rf = RandomForestClassifier(n_estimators=100)

modelo_rf.fit(X_train,y_train)

# Teste

score = modelo_rf.score(X_test,y_test)
print('A exatidão do modelo é: ',score)


# Gradient Boosting

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

iris

#Treinamento
#base 
X = pd.DataFrame(iris.data, columns=iris.feature_names) #Treinamento/  Objeto que vai gerar a previsão
y = pd.Series(iris.target) #Teste/ Target é o objetivo a ser previsto

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

#modelo
modelo_gb = GradientBoostingClassifier()

modelo_gb.fit(X_train, y_train)

#Accuracy
acuracia = modelo_gb.score(X_test,y_test)

print('Acurácia do modelo: ',acuracia)

# Desafio Resposta

nova_flor = [7.0,1.0,2.5,0.2]
previsao = modelo_gb.predict([nova_flor])
print('Espécie de flor prevista com base nos valores entregues: ', iris.target_names[previsao][0])


# Introdução a Redes Neurais Artificiais

#Apresentação do VQGAN + Clip














# Avaliação de Modelos de Aprendizado de Máquina

#Avaliação de Modelos

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

comprimento = [1.4,1.3,1.5,4.7,4.5,4.9,5.1,6.0,5.8,6.6,6.9,5.7,6.3,6.1]
largura = [0.2,0.3,0.1,1.4,1.5,1.5,1.8,2.5,2.3,2.1,2.3,2.8,2.5,2.8]

comprimento
largura

classe = ['setosa','setosa','setosa','versicolor','versicolor','versicolor','versicolor',
          'virginica','virginica','virginica','virginica','virginica','virginica','virginica']

df_flores = pd.DataFrame({'comprimento': comprimento,'largura':largura,'classe':classe})

df_flores

modelo_KN = KNeighborsClassifier(n_neighbors=3)

X = df_flores[['comprimento','largura']]
y = df_flores['classe']
modelo_KN.fit(X, y)

nova_amostra = [[7.03,3.0]]
previsao = modelo_KN.predict(nova_amostra)

print('A nova nova flor pertence à classe: ',previsao[0])

# Avaliação do modelo

y_pred = modelo_KN.predict(X)
print('Acurácia:', accuracy_score(y, y_pred))
print('Matriz de confusão:',confusion_matrix(y,y_pred))
print('Relatório de Classificação', classification_report(y,y_pred))











