lista_musicas  = []

while True:
    print("\n1 - Adicionar musica")
    print("2 - Remover música por nome ou posição")
    print("3 - Visualizar Playlist")
    print("4 - Visualizar a posição da música")
    print("5 - Inverter a ordem da música")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case '1':
            musica = input("Digite a música que deseja adicionar: ")
            lista_musicas.append(musica)
            print("Música adicionada com sucesso!")

        case '2':
            remover_indice_nome = int(input('deseja remover por nome ou posição \n 1 - nome \n 2 - posição \n\nEscolha uma opção: '));
            if remover_indice_nome == 1:
                remover  = input('Digite o nome da música a ser excluida: ')
                removido = lista_musicas.remove(remover)
                print(f"música {remover}' excluída com sucesso!")
            elif remover_indice_nome == 2:
                indice  = int(input('Digite a posição da música a ser excluida: '))
                lista_musicas.pop(indice)
                print(f"música {indice}' excluída com sucesso!")
            else:
                print("Não existem músicas na sua Playlist!")

        case '3':
            if lista_musicas:  # Verifica se a lista não está vazia
                for i, musica in enumerate(lista_musicas, start=1):
                    print(f"música {i} - {musica}")
            else:
                print("Não existem músicas na sua Playlist!")
           
        case '4':
             localizar_musica = input('Digite o nome da música: ')
             posicao = lista_musicas.index(localizar_musica)
             print(f'A música {localizar_musica} está na posição {posicao+1} da playlist')
        case '5':
             lista_musicas.reverse()
             print('Playlist invertida.')
             
                
        case '0':
            print("Saindo do sistema. Obrigado por curtir nos playlist!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
