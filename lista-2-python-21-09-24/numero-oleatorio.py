""" 4) Escreva um programa que gera um número aleatório entre 1 e 100 e permite
que o usuário tente adivinhá-lo. O programa deve informar se o palpite é maior
ou menor que o número gerado. Use um loop while para permitir que o usuário
faça múltiplos palpites. Dica: Utilize a variável numero_secreto =
random.randint(1, 100) para gerar o número aleatório. """
import random

tentativas = 0
numero_secreto = random.randint(1, 100)
print('\nBEM-VINDO AO JOGO ADVINHAÇÃO!\n\nTENTE ACERTAR O NÚMERO EM POUCAS CHANCES!')
# teste 
# print(numero_secreto)

while True: 
    palpite = int(input('Qual o seu palpite: '))
    tentativas += 1
    if palpite > 100 or palpite < 1: 
        print('\nOps valor inválido, Informe um valor de 1 a 100.\n')
    elif palpite < numero_secreto:
        print(f'\nO número secreto é maior que {palpite} e seu número de tentativas é {tentativas}.\n')
    elif palpite > numero_secreto:
        print(f'\nO número secreto é menor que {palpite} e seu número de tentativas é {tentativas}.\n')
    else:
        print(f'\nParabéns, você acertou :) O número sorteado foi {numero_secreto} e seu número de tentativas é {tentativas}.\n')
        break
