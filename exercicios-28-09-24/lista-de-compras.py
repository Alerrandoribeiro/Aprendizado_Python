compras = []

print("===== LISTA DE COMPRAS =====")

while True:
    print("\n1 - Adicionar itens")
    print("2 - Remover itens")
    print("3 - Visualizar itens")
    print("4 - Contar quantidade de produtos específicos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case '1':
            item = input("Digite o item que deseja adicionar: ")
            compras.append(item)
            print("item adicionado!")

        case '2':
            if compras:
                remover  = input('Digite o item a ser removido: ')
                removido = compras.remove(remover)
                print(f"item '{remover}' removido!")
            else:
                print("Não existem itens adicionados!")

        case '3':
            if compras:  # Verifica se a lista não está vazia
                for i, item in enumerate(compras, start=1):
                    print(f"Item {i} - {item}")
            else:
                print("Sua lista não possui itens!")

        case '4':
            if compras:  
                qtd = input('Informe o item a ser contado: ')
                quantidade = compras.count(qtd)
                print(f"A quantidade de '{qtd}' é: {quantidade}")
            else:
                print("Adicione pelo menos um item!")

        case '0':
            print("Saindo do sistema. Obrigado pela compra!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
