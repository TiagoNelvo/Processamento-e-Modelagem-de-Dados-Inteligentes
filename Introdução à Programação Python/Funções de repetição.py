lista = ["Python", "é", "uma", "linguagem", "de", "programação", "."]

lista
print(lista)
lista[1]

# Iteração com "for"

for i in lista:
    print(i)
    
nome_empresa = "Edugital"
numero_funcionario = 100
faturamento_anual = 1000000000000.00
empresa_aberta = True
custos_anuais = 9999.99

def calcular_lucro(faturamento_anual, custos_anuais):
    faturamento = faturamento_anual / 12
    custos = custos_anuais / 12
    lucro = faturamento - custos
    return lucro

calcular_lucro(faturamento_anual, custos_anuais)
calcular_lucro(10000, 1000)