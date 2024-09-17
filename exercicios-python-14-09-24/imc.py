""" 6 - Criar um programa que calcule o IMC, no qual o usuário deve digitar o seu peso e altura, realizar o cálculo (peso / altura * altura) e mostrar o resultado na tela, com 3 casas depois da vírgula.  */
let altura, peso """

def imc(peso,altura): #
    return peso /(altura * altura)

print('CALCULADORA DE IMC(ÍNDICE DE MASSA CORPORAL')

peso = float(input('Digite seu peso em kg: '));
altura = float(input('Digite sua altura em metros: '));

print(f'O índice de massa muscular é {imc(peso,altura):.3f}') # formatando com três casas decimais depois da vírgula.




   