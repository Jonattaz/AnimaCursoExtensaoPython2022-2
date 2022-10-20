# Primeiro projeto python!!!
'''Comentario em bloco'''

print("Alo mundo!\n")

# Não precisa declarar o tipo de variável
# String
nome = "Jonatas"
sobrenome = "Santos"
# Integer
idade = 21

# Float
dinheiro = 200000.45

print("R${}\n".format(dinheiro))

# 1.Conversão - str()
print(nome + " " + sobrenome + " " + str(idade) + " anos de idade\n")

# 2.Conversão - f"{}"
print(nome + f" possui {idade}" + " anos de idade\n");

# 3.Conversão - .format(idade)
print("Senhor " +sobrenome +" possui "+ "{} anos de idade".format(idade))

