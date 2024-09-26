""" 3) Crie um programa que solicita ao usuário uma nota (de 0 a 10) e exibe a
mensagem correspondente:
"Aprovado" se a nota for 7 ou maior.
"Em recuperação" se a nota estiver entre 4 e 6.
"Reprovado" se a nota for menor que 4. """

numero = float(input('Informe uma nota de 0 a 10: '));

while( numero < 0 or numero > 10):
    print('Ops. Digite um valor válido! ')
    numero = float(input('Informe uma nota de 0 a 10: '));
match numero: 
    case _ if numero >= 7: 
        print(f'Aprovado com nota {numero}')
    case _ if numero >= 4: 
        print(f'Em recuperação {numero}')
    case _: 
        print(f'Reprovado')