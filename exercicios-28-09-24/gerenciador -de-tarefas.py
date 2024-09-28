lista_tarefas  = []

while True:
    print("\n1 - Adicionar uma tarefa")
    print("2 - Remover tarefas comcluídas")
    print("3 - Visualizar tarefas pendentes")
    print("4 - Adicionar tarefas na posição desejada da lista")
    print("5 - quantidade de vezes que a tarefa foi realizada")
    print("6 - Ordenando tarefas por ordem alfabética")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case '1':
            tarefa = input("Informe o mome da tarefa que deseja adicionar: ")
            lista_tarefas.append(tarefa)
            print("tarefa adicionada com sucesso!")

        case '2':
            removendo_tarefas_concluidas= int(input('deseja remover a tarefa por nome ou posição \n 1 - nome \n 2 - posição \n\nEscolha uma opção: '));
            if removendo_tarefas_concluidas == 1:
                remover  = input('Digite o nome da tarefa a ser excluida: ')
                removido = lista_tarefas.remove(remover)
                print(f"tarefa {remover}' excluída com sucesso!")
            elif removendo_tarefas_concluidas == 2:
                indice  = int(input('Digite a posição da tarefa a ser excluida: '))
                lista_tarefas.pop(indice)
                print(f"tarefa {indice}' excluída com sucesso!")
            else:
                print("Não existem mais tarefas sua lista!")

        case '3':
            if lista_tarefas:  # Verifica se a lista não está vazia
                for i, tarefa in enumerate(lista_tarefas, start=1):
                    print(f"tarefa {i} - {tarefa}")
            else:
                print("Não existem mais tarefas sua lista!")
           
        case '4':
             localizar_tarefa = input('Digite o nome da tarefa: ')
             posicao = lista_tarefas.index(localizar_tarefa)
             print(f'A tarefa {localizar_tarefa} está na posição {posicao+1} da sua lista')
             
             nova_tarefa = input("Informe o mome da da nova tarefa que deseja adicionar: ")
             lista_tarefas.index(posicao).append(nova_tarefa)
             print("tarefa adicionada com sucesso!")
    
        case '5':
             lista_musicas.reverse()
             print('Playlist invertida.')
             
                
        case '0':
            print("Saindo do sistema. Obrigado por curtir nos playlist!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
