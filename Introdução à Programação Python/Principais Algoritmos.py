# Algoritmo de pesquisa binária
lista_numeros = [2, 3, 4, 5, 8, 10]
numero_pesquisado = 5

inicio = 0
fim = len(lista_numeros) - 1
encontrado = False

while inicio <= fim and not encontrado:
    meio = (inicio + fim) // 2
    if lista_numeros[meio] == numero_pesquisado:
        encontrado = True
    elif numero_pesquisado < lista_numeros[meio]:
        fim = meio - 1
    else:
        inicio = meio + 1

if encontrado:
    print("O número ", numero_pesquisado, "Foi encontrado na lista")
else:
    print("O número: ", numero_pesquisado, "Não foi encontrado na lista")
    