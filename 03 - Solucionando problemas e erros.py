
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