### ----------- Laço -------------- ###
# For
# Contar de 1 até 10
print("----- Contador ----")
contador = 0
while (contador < 10):
  contador += 1
  print(contador)

print("\n")
# Contar de 10 até 0
while (contador > 0):
  contador -= 1
  print(contador)


print("\n")  
# Lista
print("----- Cesta de frutas ----")
cesta = ["Morango", "laranja", "Pêra"]
print("Na cesta existem essas frutas: " + str(cesta))
print("\nSua fruta favorita é: " + str(cesta[0]))

## Adicionar mais uma fruta
cesta.append("Manga");

# Exibe o número de frutas que existem na lista
print("\nNúmero de frutas na cesta: " + str(len(cesta)))

print("\nNa cesta existem essas frutas: ")
i = 0
while(i < len(cesta)):
  print(cesta[i])
  i += 1

print("\nFrutas que como durante a semana: ")  
# For each
for frutas in cesta:
  print(frutas)



### ----------- Funções -------------- ###
# Função para calcular um imposto de 5%
print("\nCalculo de imposto de renda")  
def Calcular_Imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto


#print("O imposto pago foi de " + str((Calcular_Imposto(299))))
valores = [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
  print("O imposto de "+ str(valor) + " é "+ str(Calcular_Imposto(valor)))


#Função que recebe dois parâmetros
def Calcular_Imposto_Aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

print("\nImposto com aliquotas diferentes")
for valor in valores:
   print("O imposto de "+ str(valor) + " é "+ str(Calcular_Imposto_Aliquota(valor, 8)))
