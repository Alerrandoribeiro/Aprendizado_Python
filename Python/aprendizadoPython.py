"""
nome = input('Qual o seu nome: ');
idade = input('Qual o sua idade: ');
print( nome ,' tem ', idade , ' anos.');

"""
""" 
idade = int(input('Qual a sua idade: '));

if idade >=18: 
  print('É maior de idade e pode votar.')
elif idade >= 16:
  print('Você pode votar, mas não é obrigatório.')
else: 
  print('você não pode votar.') 
    
"""
""" 
numero = int(input('Informe um numero:'));

if numero > 10:
  print('Esse número é maior que 10.')
else:
    print('Esse número é menor ou igual a 10.')
    
"""   
"""

idade = int(input('Qual a sua idade: '));
if idade >=18: 
  print('É maior de idade e pode votar.')
elif idade >= 16:
  print('Você pode votar, mas não é obrigatório.')
else: 
  print('você não pode votar.')
  
"""
"""
nome = input('Qual o seu nome: ');
sobrenome = input('Qual o seu sobrenome: ');
nome_completo = nome + " " + sobrenome

print('Seu nome completo é ' + nome_completo)

"""
"""
numero_um = int(input('Informe o primeiro valor: '));
numero_dois = int(input('Informe o segundo valor: '));

soma = numero_um + numero_dois;             
subtracao = numero_um - numero_dois; 
multiplicacao = numero_um * numero_dois;
divisao = numero_um / numero_dois;
resto = numero_um % numero_dois;

print('A soma de', numero_um, 'e', numero_dois ,'é' , soma);
print('A subtração de', numero_um, 'e', numero_dois ,'é' , subtracao);
print('A multiplicação de', numero_um, 'e', numero_dois ,'é' , multiplicacao);
print('A divisão de', numero_um, 'e', numero_dois ,'é' , divisao);
print('O resto da divisão de', numero_um, 'e', numero_dois ,'é' , resto);

"""
"""
idade = int(input('Qual a sua idade: '));
altura = float(input('Qual a sua altura: '));
nome = str(input('Qual seu nome: '));
profissao = str(input('Qual sua profissão: '));
print(' Idade: ',idade, '\n Altura: ' ,altura, ' \n Nome: ' , nome, '\n Profissão: ' ,profissao)

print(type(idade))
print(type(altura))
print(type(profissao))

"""
"""
numero = int(input('Digite um número de 1 a 3: '));

match numero:
  case 1:
    print('Opção 1')
  case 2:
    print('Opção 2')
  case 3:
    print('Opção 3')
  case  _:
    print('Número não é válido!')
    
"""
"""
numero = int(input('Digite um número de 1 a 3: '));

match numero:
  case 1 | 2 | 3 :
    print(f'número {numero} é válido.')
  case _:
    print(f'O valor {numero} é inválido.')
""" 
"""   
numero_a = int(input('Digite o número a: '));
numero_b = int(input('Digite o número b: '));
opcao = int(input('Escolha a opção: \n1 - Soma \n2 - subtração \n3 - divisão \n4 - Multiplicacao \n\nDigite um valor: '));

match opcao:
  case 1:
    soma = numero_a + numero_b;
    print(f' A soma de {numero_a} e {numero_b} é {soma}')
  case 2:
    subtracao = numero_a - numero_b;
    print(f' A subtração de {numero_a} e {numero_b} é {subtracao}')
  case 3:
    divisao = numero_a / numero_b;
    print(f' A divisão de {numero_a} e {numero_b} é {divisao}')
  case 4:
    multiplicacao = numero_a * numero_b;
    print(f' A multiplicação de {numero_a} e {numero_b} é {multiplicacao}')
  case  _:
    print('Informe um valor válido!')

"""
"""

numero = int(input('qual é o número ? '));

if numero >= 10 and numero <= 20:
  print('Está dentro do intervalo.');
else:
     print('Não está dentro do intervalo.');

"""
"""

feriado = input('Hoje é feriado ? \nsim\nnão \n\ninforme sua resposta:').lower();  
fim_de_semana = input('Hoje é final de semana ? \nsim\nnão \n\ninforme sua resposta:').lower(); 

if feriado == 'sim' or fim_de_semana == 'sim' : 
  print('\nHoje é dia de descanso!')
else:
  print('\nHoje é dia de trabalho!')
  
"""
"""

temperatura = float(input('Informe a temperatura atual: '));
esta_chovendo = input('Está chovendo ? \nsim\nnão \n\ninforme sua resposta: ').lower();

if (temperatura >=20 and temperatura <=30) and esta_chovendo == 'não':

   print('\nDia agradável para pasear. :)')
else:
    print('\nTalvez melhor ficar em casa. :( ')
 
"""
"""
senha = 1234;
nome = "admin";

usuario = input('Informe seu usuário: ');
senha_digitada = int(input('Informe sua senha: '));

if(senha_digitada == senha and nome == usuario):
  print('acesso concedido.')
else:
  print('Acesso negado.')  

"""
"""
frutas = ['maça', 'banana', 'cereja'];

for frutas in frutas:
  print(frutas)

"""
"""
contador = 1;
while contador <= 5:
  print(contador) 
  contador+=1

"""

""" # range(stop) vai de 0 a 4

for i in range(5):
   print(i)

# range(start,stop) vai de 2 até 6 

for i in range(2, 6):
   print(i)

# range(start,stop,step) vai pulando de 2 em dois

for i in range(1, 10, 2): 
   print(i)



texto = input("qual a palavra: ")

for letra in texto:
  print(letra)



 # range(stop) vai de 0 a 9

for i in range(1,11):
   print(i)


cont = 1
while(cont <= 10):
  print(cont)
  cont +=1   

"""  