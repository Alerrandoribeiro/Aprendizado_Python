""" 3) Implemente um sistema de gestão de vendas que permita registrar vendas de 
produtos e calcular estatísticas relacionadas. O sistema deve permitir as seguintes 
operações: 
1. Adicionar Produtos: Adicionar novos produtos à lista de produtos disponíveis 
para venda, com nome, preço e quantidade em estoque. 
2. Registrar Venda: Registrar uma venda, diminuindo a quantidade de um 
produto no estoque e adicionando a venda a uma lista de vendas. 
3. Exibir Produtos Disponíveis: Exibir todos os produtos com quantidade 
disponível em estoque. 
4. Exibir Vendas Realizadas: Exibir todas as vendas realizadas, com detalhes sobre 
o produto vendido, a quantidade e o valor total da venda. 
5. Calcular Receita Total: Calcular a receita total gerada pelas vendas realizadas. 
6. Identificar Produto Mais Vendido: Identificar o produto que gerou o maior 
valor em vendas. 
7. Reabastecer Estoque: Permitir o reabastecimento de produtos no estoque.
"""
produtos = []
vendas = []

while True:
    print("\nSistema de Gestão de Vendas")
    print("1. Adicionar Produtos")
    print("2. Registrar Venda")
    print("3. Exibir Produtos Disponíveis")
    print("4. Exibir Vendas Realizadas")
    print("5. Calcular Receita Total")
    print("6. Identificar Produto Mais Vendido")
    print("7. Reabastecer Estoque")
    print("8. Sair")
    
    opcao = input("Escolha uma opção (1-8): ")

    if opcao == '1':
        # aqui eu Adiciono os produtos
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        produtos.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})
        print(f"Produto '{nome}' adicionado com sucesso!")

    elif opcao == '2':
        # aqui eu Registro as Vendas
        nome = input("Digite o nome do produto vendido: ")
        for produto in produtos:
            if produto['nome'] == nome:
                if produto['quantidade'] > 0:
                    quantidade_vendida = int(input("Digite a quantidade vendida: "))
                    if quantidade_vendida <= produto['quantidade']:
                        produto['quantidade'] -= quantidade_vendida
                        valor_venda = quantidade_vendida * produto['preco']
                        vendas.append({'produto': nome, 'quantidade': quantidade_vendida, 'valor': valor_venda})
                        print(f"Venda registrada: {quantidade_vendida} de '{nome}' por R${valor_venda:.2f}.")
                    else:
                        print("Quantidade vendida maior que a disponível em estoque.")
                else:
                    print("Produto fora de estoque.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == '3':
        # aqui mostro todos os produtos disponíveis
        print("\nProdutos disponíveis:")
        for produto in produtos:
            print(f"{produto['nome']} - Preço: R${produto['preco']:.2f} - Estoque: {produto['quantidade']}")

    elif opcao == '4':
        # aque mostra todas as vendas realizadas
        print("\nVendas realizadas:")
        for venda in vendas:
            print(f"Produto: {venda['produto']} - Quantidade: {venda['quantidade']} - Valor Total: R${venda['valor']:.2f}")

    elif opcao == '5':
        # aqui eu Calculo Receita Total
        receita_total = sum(venda['valor'] for venda in vendas)
        print(f"\nReceita total: R${receita_total:.2f}")

    elif opcao == '6':
        # aqui eu Identifico Produto Mais Vendido
        vendas_por_produto = {}
        for venda in vendas:
            nome = venda['produto']
            if nome not in vendas_por_produto:
                vendas_por_produto[nome] = 0
            vendas_por_produto[nome] += venda['valor']
        
        if vendas_por_produto:
            produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
            print(f"\nProduto mais vendido: {produto_mais_vendido} - Receita: R${vendas_por_produto[produto_mais_vendido]:.2f}")
        else:
            print("Nenhuma venda registrada.")

    elif opcao == '7':
        # código para reabastecer Estoque
        nome = input("Digite o nome do produto a reabastecer: ")
        for produto in produtos:
            if produto['nome'] == nome:
                quantidade_adicionada = int(input("Digite a quantidade a ser adicionada: "))
                produto['quantidade'] += quantidade_adicionada
                print(f"Estoque de '{nome}' reabastecido com {quantidade_adicionada} unidades.")
                break
        else:
            print("Produto não encontrado.")

    elif opcao == '8':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida! Tente novamente.")
