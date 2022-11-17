#Importar biblioteca
import sqlite3

#Estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#Criar um objeto do tipo cursor
cursor = conexao.cursor()

#Comando SQL do banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#Executar o comando SQL no SQLlite
cursor.execute(sql)

#Exibir todos os nomes dos heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} - {pessoa[3]}")

#Comando para inserir herói ou vilão
#sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Wally West', 'Herói(na)')"

#Executar o comando SQL
#print(cursor.execute(sql))

#Confirmar o INSERT com commit() e fechar o banco
#conexao.commit()
#conexao.close()

#Importar a biblioteca sqlite3
import sqlite3


#Função conectar()
def conectar():
  #Conexão com o banco de dados
  conexao = sqlite3.connect("dc_universe.db")

  #Criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor


nome = input("Informe o nome do herói/vilão: ")
nome_civil= input("Informe o nome civil do herói/vilão: ")
tipo_numerico = input("Tecle 1 para herói(na) ou 2 para vilã(o)")

#Consulta para o valor máximo usado no banco
sql = "SELECT MAX(pessoa_id)+1 FROM pessoas"
cursor.execute(sql)
pessoa_id = cursor.fetchone()[0]

if(tipo_numerico == "1"):
  tipo = "Herói(na)"
else:
  tipo = "Vilã(o)"

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')"

cursor.execute(sql)
conexao.commit()
conexao.close()













