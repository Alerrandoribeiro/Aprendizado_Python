"""5) Uma pousada cobra R$280 reais a diária por quarto e R$15 reais o café por pessoa por dia.
Você pretende passar um tempo com alguns amigos nessa pousada, sendo que todos ficarão no
mesmo quarto. Informar a quantidade de pessoas, o número de diárias e quantas pessoas do
grupo vão querer café diário. Mostrar na tela o total a pagar."""

diaria_por_quarto = 280;
cafe_pessoa_por_dia = 15;
total_pagar = 0;

quantidade_pessoas = int(input('Digite a quantidade de pessoas: '));
numero_de_diarias = int(input('Informe o número de diárias: '));
quantidade_de_pessoas_que_querem_cafe = int(input('Informe o quantas pessoas querem café: '));

total_pagar = (diaria_por_quarto * numero_de_diarias) + (cafe_pessoa_por_dia * quantidade_de_pessoas_que_querem_cafe);

print(f'O valor a pagar é {total_pagar} reais.')


# Glauberty Alerrando Chagas Ribeiro