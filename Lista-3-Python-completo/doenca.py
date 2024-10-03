""" 2) Desenvolver um programa que peça ao usuário o número de doenças a cadastrar, 
no qual ele deve cadastrar o nome da doença e se ela é transmitida por vírus, bactéria 
ou por ambos. Ao final, mostrar quatro listas: doenças transmitidas por vírus, doenças 
transmitidas por bactérias, doenças transmitidas por ambos, lista com todas doenças.
"""
num_doencas = int(input("Quantas doenças você deseja cadastrar? "))

doencas_virus = []
doencas_bacteria = []
doencas_ambos = []
todas_doencas = []

for _ in range(num_doencas):
    nome_doenca = input("Digite o nome da doença: ")
    tipo_transmissao = input("A doença é transmitida por (1) vírus, (2) bactéria ou (3) ambos? ")


    todas_doencas.append(nome_doenca)
    if tipo_transmissao == '1':
        doencas_virus.append(nome_doenca)
    elif tipo_transmissao == '2':
        doencas_bacteria.append(nome_doenca)
    elif tipo_transmissao == '3':
        doencas_ambos.append(nome_doenca)
    else:
        print("Opção inválida! A doença não será adicionada.")


print("\nDoenças transmitidas por vírus:")
print(doencas_virus)

print("\nDoenças transmitidas por bactérias:")
print(doencas_bacteria)

print("\nDoenças transmitidas por ambos:")
print(doencas_ambos)

print("\nLista de todas as doenças:")
print(todas_doencas)
