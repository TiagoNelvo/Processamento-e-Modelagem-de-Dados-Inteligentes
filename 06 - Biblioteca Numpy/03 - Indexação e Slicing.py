import numpy as np


array_1 = np.array([1,1,1])
array_2 = np.array([2,2,2])

array_1
array_2
soma_array = array_1 + array_2
soma_array

array_2[2]

np.append(array_1,array_2)

nova_array = np.append(array_1,array_2)
nova_array

nova_array[3]

# Slicing / Fatiamento

print(nova_array[0:4])

np.sin(nova_array)

seno_array = np.sin(nova_array)

seno_array

np.exp(seno_array)

# Operações Avançadas

media_array = np.mean(nova_array)
media_array

mediana_array = np.median(nova_array)
mediana_array

desvio_padrao = np.std(nova_array)
desvio_padrao