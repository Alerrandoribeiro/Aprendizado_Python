"""" 1 - Crie um programa que peça os dados de um cliente: Nome, idade, nacionalidade,
  endereço. Após digitados os dados, mostrar na tela a seguinte mensagem "Cliente [Nome], com [idade] anos,
  [nacionalidade], reside no endereço [endereço]". Exemplo: Cliente Lucas, com 29 anos, brasileiro,
  reside no endereço Rua Victor Meirelles, 281, Centro, Florianópolis.  """

nome =  input('Digite seu nome: ');
idade = int(input('Digite idade: '));
nacionalidade = input('Digite sua nacionalidade: ');
endereco = input('Digite seu endereço: ');

print(f'Cliente' , nome , 'com' , idade , 'anos de idade,' , nacionalidade , 'reside no endereço' , endereco,'.');