""" 4) Você foi contratado para desenvolver um sistema simples de gerenciamento de 
produtos para uma loja. O objetivo é criar um programa que permita a um usuário 
realizar as seguintes operações em uma lista de produtos: 
1. Cadastrar Produto: O usuário deve poder inserir o nome e o preço de um novo 
produto. O produto deve ser armazenado em uma lista de dicionários, onde 
cada dicionário representa um produto com suas informações. 
2. Editar Produto: O usuário deve poder modificar o preço de um produto 
existente. Para isso, o programa deve solicitar o nome do produto que deseja 
editar e, caso ele exista, permitir que o usuário atualize o preço. 
3. Excluir Produto: O usuário deve ter a opção de remover um produto da lista 
informando o nome do produto a ser excluído. 
4. Listar Produtos: O programa deve exibir todos os produtos cadastrados, 
mostrando o nome e o preço de cada um. 
5. Sair: O usuário deve poder sair do sistema a qualquer momento.
"""

produtos = []

while True:
    print("\nSistema de Gerenciamento de Produtos")
    print("1. Cadastrar Produto")
    print("2. Editar Produto")
    print("3. Excluir Produto")
    print("4. Listar Produtos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        produtos.append({'nome': nome, 'preco': preco})
        print(f"Produto '{nome}' cadastrado com sucesso!")

    elif opcao == '2':
        nome = input("Digite o nome do produto que deseja editar: ")
        for produto in produtos:
            if produto['nome'] == nome:
                novo_preco = float(input("Digite o novo preço do produto: "))
                produto['preco'] = novo_preco
                print(f"Preço do produto '{nome}' atualizado para R${novo_preco:.2f}.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == '3':
        nome = input("Digite o nome do produto que deseja excluir: ")
        for produto in produtos:
            if produto['nome'] == nome:
                produtos.remove(produto)
                print(f"Produto '{nome}' excluído com sucesso.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == '4':
        if produtos:
            print("\nProdutos cadastrados:")
            for produto in produtos:
                print(f"Nome: {produto['nome']} - Preço: R${produto['preco']:.2f}")
        else:
            print("Nenhum produto cadastrado.")

    elif opcao == '5':
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida! Tente novamente.")
