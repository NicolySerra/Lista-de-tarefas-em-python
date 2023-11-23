#projeto lista de tarefas
from datetime import datetime

def validar_data(data_hora):
    try:
        datetime.strptime(data_hora, "%d/%m%y %H:%M")
        return True
    except:
        return False
    
def adicionar_tarefas(nome, descricao, data, hora, lista):
    lista.append(nome + ";" + descricao + ";" + data + ";" + hora)

lista = []


print("ola, bem-vindo ao meu projeto!")
while True:
    print("MENU:")
    print("1. Adicionar uma tarefa")
    print("2. Listar tarefa")
    print("3. Remover uma tarefa")
    print("4. Editar uma tarefa")
    print("5. Sair")

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("opçao invalida")
        continue

    if(escolha == 1):
        nome_tarefa = input("digite o nome da tarefa: ")
        descricao_tarefa = input("digite a descriçao da tarefa: ")
        data_tarefa = input("digite a data em formato dia/mes/ano: ")
        hora_tarefa = input("digite uma hora em formato hora:min: ")

        data_hora = data_tarefa + " " + hora_tarefa

        if(validar_data(data_hora)):
            adicionar_tarefas(nome_tarefa, descricao_tarefa, data_tarefa, hora_tarefa, lista)
            print(lista)
        else:
            print("erro, data invalida")
 
 