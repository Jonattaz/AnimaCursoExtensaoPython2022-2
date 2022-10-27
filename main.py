# O main é usado apenas para praticar durante a aula, depois o conteúdo que está aqui é colocado no arquivo que contém a sua data

# Comando de entrada para permitir que o usuário digite algo. input()
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

# Comando de saída
print("Bem vindo " + nome)
print("Sua idade é: " + str(idade))

dobro = idade * 2

print("O dobro da sua idade é: " + str(dobro))

# Estrutura condicioonal
#If
if idade >= 18:
  print(
    "Você é maior de idade, lembre-se que com grandes poderes vem grandes responsabilidades"
  )
else:
  print("Você ainda é menor de idade, se divirta e aprenda o máximo que puder")

# Perguntando o gênero(M = masculino e F = feminino) e caso seja masculino mostrar se fez serviço militar obrigatório
genero = input(
  "Digite um gênero, sendo M para masculino, F para feminino e O para outros: "
)

if idade >= 18 and genero == "M":
  print("Você precisa ou precisou prestar serviço militar obrigatório")

  ## ---------- Nota do aluno -------------- ##

aluno = input("Escreva o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 0 and nota < 7:
  print(aluno + " está de recuperação")
elif nota >= 7 and nota < 10:
  print(aluno + " aluno está com uma boa nota")
elif nota == 10:
  print(aluno + " tirou a nota máxima, parabenize ele pelo bom trabalho")
else:
  print("A nota digitada possui algum erro")

### ----------- Laço -------------- ###
# Exibir números de 1 a 10
numero = 0;

while numero < 10:
  numero += 1
  print(numero)
  














