""" 2) Escreva uma função chamada converter_temperatura que receba uma
temperatura em graus Celsius como parâmetro e retorne a temperatura
convertida para Fahrenheit. Use a fórmula F=C×95+32F = C \times \frac{9}{5} +
32F=C×59 +32. Exiba o resultado fora da função. """

def converter_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input('Digite a temperatura em graus Celsius: '))

temperatura_fahrenheit = converter_temperatura(temperatura_celsius)
print(f'A temperatura {temperatura_celsius} °C em Fahrenheit é: {temperatura_fahrenheit:.2f} °F')

