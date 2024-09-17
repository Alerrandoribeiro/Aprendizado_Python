""" 2 - Faça um programa no qual o usuário digite dois números e mostre na tela a multiplicação desses números."""

def multiplica(n1,n2):
    return n1 * n2 

print('Calculadora de multiplicação');
numeroUm = int(input('digite o primeiro número: '));
numeroDois = int(input('digite o segundo número: '));
print(f'A multiplicação entre {numeroUm} e {numeroDois} é {multiplica(numeroUm,numeroDois)}.');


