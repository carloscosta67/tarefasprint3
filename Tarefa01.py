# Importa as funções necessárias
from login import login
from aluno import aluno
from professor import professor
from adm import adm

# Função principal
def menu():
  # Chama a função de login
  tipo_usuario = login()

  # Chama a função correspondente ao tipo de usuário
  if tipo_usuario == "aluno":
    aluno()
  elif tipo_usuario == "professor":
    professor()
  elif tipo_usuario == "adm":
    adm()

# Chama a função principal
menu()