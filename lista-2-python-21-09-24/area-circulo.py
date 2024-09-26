""" 1) Crie uma função chamada calcular_area_circulo que receba o raio de um
círculo como parâmetro e retorne a área do círculo (use a fórmula A = π * r²,
onde π pode ser aproximadamente 3.14). Exiba o resultado fora da função. """

def calcular_area_circulo(raio):
    pi = 3.14
    area = pi * (raio * raio)
    return area

numero = float(input('Digite o raio do círculo: '))

# Converta o resultado para string para a concatenação
print(f'A área do círculo é: {calcular_area_circulo(numero):.2f}')
