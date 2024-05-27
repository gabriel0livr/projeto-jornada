import os
import json

def salvar_dados(lista):
    with open('alunos.json', 'w') as arquivo:
        json.dump(lista, arquivo)

def carregar_dados():
    try:
        with open('alunos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def adicionar_aluno(lista):
    os.system('cls')
    nome_aluno = input('Nome do aluno: ')
    nome_responsavel = input('Nome do responsável: ')
    cpf = input('CPF do responsável: ')
    telefone = input('Celular do responsável: ')
    endereco = input('Endereço do aluno: ')
    lista.append({'nome_aluno': nome_aluno,'nome_responsavel': nome_responsavel,'cpf': cpf,'telefone': telefone, 'endereco': endereco})
    salvar_dados(lista)
    print("Aluno adicionado com sucesso!")

def excluir_aluno(lista):
    nome_excluir = input("Qual aluno você quer excluir? ")
    
    for aluno in lista:
        if aluno['nome_aluno'] == nome_excluir:
            lista.remove(aluno)
            salvar_dados(lista)
            print("Aluno excluído com sucesso!")
            break
        else:
            print("Aluno não encontrado.")

def listar_alunos(lista):
    for indice, aluno in enumerate(lista):
        print(aluno['nome_aluno'], "-", aluno['telefone'])

def atualizar_aluno(lista):
    nome_atualizar = input("Qual aluno você quer atualizar? ")
    for aluno in lista:
        if aluno['nome_aluno'] == nome_atualizar:
            novo_nome_aluno = input("Novo nome do aluno: ")
            novo_nome_resp = input("Novo nome do responsavel: ")
            novo_endereco = input("Novo endereço do aluno: ")
            novo_cpf = input("Novo cpf: ")
            novo_telefone = input("Novo telefone:")

            aluno['nome_aluno'] = novo_nome_aluno
            aluno['nome_responsavel'] = novo_nome_resp
            aluno['endereco'] = novo_endereco
            aluno['cpf'] = novo_cpf
            aluno['telefone'] = novo_telefone
            
            salvar_dados(lista)
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

lista = carregar_dados()

while True:
 print("Selecione uma opção:")
 resposta = input("1 - Área Do Aluno\n2 - Informar Ida ao Colégio\n3 - Chat\n4 - Avaliar Serviço\n5 - Sair\nOpção: ")

 if resposta == '1':
     os.system('cls')
     while True:
      print("Área do Aluno🚌")
      resposta = input("1 - Adicionar Aluno\n2 - Excluir Aluno\n3 - Listar Alunos\n4 - Atualizar Aluno\n5 - Sair\nOpção: ")

      if resposta == "1":
        adicionar_aluno(lista)

      elif resposta == "2":
        excluir_aluno(lista)

      elif resposta == "3":
        listar_alunos(lista)

      elif resposta == "4":
        atualizar_aluno(lista)

      elif resposta == "5":
        print("Programa finalizado.")
        break

      else:
        print("Resposta inválida.")

 elif resposta == '2':
    os.system('cls')
    print("Ida ao colegio notificada com sucesso!✅")
     #mensagem fictícia
 elif resposta == '3':
    os.system('cls')
    print("Ainda estamos trabalhando nisso...⏳")

 elif resposta == '4':
    os.system('cls')
    print("Ainda estamos trabalhando nisso...⏳")
    

 elif resposta == '5':
    os.system('cls')
    print("Programa finalizado ❌ ")
    break