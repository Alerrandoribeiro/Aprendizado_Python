""" 1) Fazer um programa que simule uma fila de lotérica. Começar uma lista vazia e dar as 
seguintes opções:  
A) Entrar pessoa (perguntar o nome) 
B) Saiu pessoa (sempre a que entrou primeiro) 
Se a fila acumular 5 pessoas, finalizar o programa e mostrar a ordem da fila 
"""

fila = []  # Lista para armazenar a fila

while True:
    print("\nMenu:")
    print("A) Entrar pessoa")
    print("B) Saiu pessoa")
    print("C) Sair do programa")
    
    opcao = input("Escolha uma opção (A, B ou C): ").strip().upper()

    if opcao == 'A':
        if len(fila) < 5:
            nome = input("Digite o nome da pessoa: ")
            fila.append(nome)
            print(f"{nome} entrou na fila.")
        else:
            print("A fila já está cheia! O programa será encerrado.")
            break

    elif opcao == 'B':
        if fila:
            pessoa_saiu = fila.pop(0)  # Remove a pessoa que entrou primeiro
            print(f"{pessoa_saiu} saiu da fila.")
        else:
            print("A fila está vazia!")

    elif opcao == 'C':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida! Tente novamente.")

# Mostrar a ordem da fila ao final
if fila:
    print("\nOrdem final da fila:")
    for pessoa in fila:
        print(pessoa)
else:
    print("A fila está vazia.")
