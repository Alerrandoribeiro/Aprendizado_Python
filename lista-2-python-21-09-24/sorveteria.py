""" 5) Uma sorveteria possui um sistema de self-service de sorvetes no qual o cliente
pode montar seu sorvete com até 4 bolas (sabores). Criar um programa que
simule esse sistema. A montagem do sorvete segue o modelo de estrutura
PILHA, onde os sabores são "empilhados" um após o outro e quando algum
tiver que ser removido, será sempre o último da pilha.
1- Adicionar sabor
2- Remover sabor
3- Visualizar sorvete
4- Finalizar pedido
======== MENSAGENS e VALIDAÇÕES ========
Opção 1-> “Sabor adicionado!” OU “Limite de sabores atingido, remova um sabor!”
Opção 2-> “Sabor removido!” OU “Não existem sabores adicionados!”
Opção 3-> “"Camada 1 - Sabor X, Camada 2 - Sabor Y, etc.” OU “Seu sorvete não
possui sabores!”
Opção 4-> “Pedido realizado!” OU “Adicione pelo menos um sabor!”
- Criar mensagem de boas-vindas e menu funcional.
- Criar uma lista para a pilha dos sabores.
- Programar a opção de "Adicionar sabor" corretamente.
- Programar a opção de "Remover sabor" corretamente.
- Programar a opção de "Visualizar sorvete" corretamente.
- Fazer as validações secundárias (lógica).
- Mostrar mensagens para o usuário (prints). """

bolas = []
limite_sabores = 4

print("===== BEM-VINDO À SORVETERIA =====")

while True:
    print("\n1 - Adicionar sabor")
    print("2 - Remover sabor")
    print("3 - Visualizar sorvete")
    print("4 - Finalizar pedido")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case '1':
            if len(bolas) < limite_sabores:
                sabor = input("Digite o sabor que deseja adicionar: ")
                bolas.append(sabor)
                print("Sabor adicionado!")
            else:
                print("Limite de sabores atingido, remova um sabor!")

        case '2':
            if bolas:
                removido = bolas.pop()
                print("Sabor removido!")
            else:
                print("Não existem sabores adicionados!")

        case '3':
            if bolas:
                for i, sabor in enumerate(reversed(bolas), start=1):
                    print(f"Camada {i} - Sabor {sabor}")
            else:
                print("Seu sorvete não possui sabores!")

        case '4':
            if bolas:
                print("Pedido realizado!")
                bolas.clear()
            else:
                print("Adicione pelo menos um sabor!")

        case '0':
            print("Saindo do sistema. Obrigado e aproveite seu sorvete!")
            break

        case _:
            print("Opção inválida. Tente novamente.")
