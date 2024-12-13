# Simulando erros


x = 10
# if x = 5: (erro: o x esta recebendo o 5, o correto é == para que seja igual ao 5)
if x == 5:
    print('O valor de x é ', x)
    
lista = [1,2,3]
#print(lista[4]) (erro: a lista compões as posições 0,1 e 2)
print(lista[2])

nums = [1,2,3,4,5]

def calcular_media(a,b,c):
    media = a + b + c / 3
    return media

# resultado = calcula_mediana(nums) (o erro esta no nome da função)
print(resultado)


# Erro

age = 30
print("I am " + age + "years old.")
age = 30
print("I am " + str(age) + "years old.")

#correção

idade = 30
type(idade)
nova_idade = str(idade)
type(nova_idade)

print("Eu tenho", idade, "anos.")
print("Eu tenho " + str(nova_idade) + " anos.")
print("Eu tenho {} anos.".format(idade))