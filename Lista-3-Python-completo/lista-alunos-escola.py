""" 5) Você deve criar um CRUD simples para gerenciar uma lista de alunos em uma escola 
utilizando um dicionário em Python. O dicionário será chamado escola, onde a chave 
será o número de matrícula do aluno e o valor será um dicionário contendo o nome, a 
idade e as notas do aluno. 
As funcionalidades do sistema devem incluir: 
1. Cadastrar um aluno (número de matrícula, nome, idade e notas). 
2. Editar as informações de um aluno. 
3. Excluir um aluno. 
4. Listar todos os alunos. 
5. Buscar um aluno pelo número de matrícula. 
6. Calcular a média das notas de um aluno. 
7. Sair do sistema.
"""

escola = {}

while True:
    print("\nSistema de Gerenciamento de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Editar Aluno")
    print("3. Excluir Aluno")
    print("4. Listar Todos os Alunos")
    print("5. Buscar Aluno por Matrícula")
    print("6. Calcular Média das Notas de um Aluno")
    print("7. Sair")
    
    opcao = input("Escolha uma opção (1-7): ")

    if opcao == '1':
       
        matricula = input("Digite o número de matrícula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        notas = list(map(float, input("Digite as notas do aluno (separadas por espaço): ").split()))
        escola[matricula] = {'nome': nome, 'idade': idade, 'notas': notas}
        print(f"Aluno '{nome}' cadastrado com sucesso!")

    elif opcao == '2':
        
        matricula = input("Digite o número de matrícula do aluno que deseja editar: ")
        if matricula in escola:
            nome = input("Digite o novo nome do aluno: ")
            idade = int(input("Digite a nova idade do aluno: "))
            notas = list(map(float, input("Digite as novas notas do aluno (separadas por espaço): ").split()))
            escola[matricula] = {'nome': nome, 'idade': idade, 'notas': notas}
            print(f"Informações do aluno '{nome}' atualizadas com sucesso.")
        else:
            print("Aluno não encontrado.")

    elif opcao == '3':
     
        matricula = input("Digite o número de matrícula do aluno que deseja excluir: ")
        if matricula in escola:
            del escola[matricula]
            print("Aluno excluído com sucesso.")
        else:
            print("Aluno não encontrado.")

    elif opcao == '4':
        
        if escola:
            print("\nAlunos cadastrados:")
            for matricula, info in escola.items():
                print(f"Matrícula: {matricula} - Nome: {info['nome']} - Idade: {info['idade']} - Notas: {info['notas']}")
        else:
            print("Nenhum aluno cadastrado.")

    elif opcao == '5':
        
        matricula = input("Digite o número de matrícula do aluno que deseja buscar: ")
        if matricula in escola:
            info = escola[matricula]
            print(f"Matrícula: {matricula} - Nome: {info['nome']} - Idade: {info['idade']} - Notas: {info['notas']}")
        else:
            print("Aluno não encontrado.")

    elif opcao == '6':
        
        matricula = input("Digite o número de matrícula do aluno: ")
        if matricula in escola:
            notas = escola[matricula]['notas']
            if notas:
                media = sum(notas) / len(notas)
                print(f"Média das notas do aluno: {media:.2f}")
            else:
                print("Nenhuma nota registrada para esse aluno.")
        else:
            print("Aluno não encontrado.")

    elif opcao == '7':
        print("Saindo do sistema.")
        break

    else:
        print("Opção inválida! Tente novamente.")
