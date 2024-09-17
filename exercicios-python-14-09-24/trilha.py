""" 3 - Você é um amante da natureza e adora fazer trilhas. Criar um programa que calcule a velocidade média das trilhas que você realiza. Para isso, devem ser digitados os dados de distância percorrida (quilômetros) e tempo que a trilha durou (horas). Fazer então o cálculo da velocidade média e mostrar na tela a mensagem "Sua média de velocidade durante essa trilha foi de X km/h", sendo X a velocidade.
 """

def velocidade_media(km,tempo):
    return km/tempo



distancia_percorrida_km = float(input('Digite a distância(KM) percorrida: '))
tempo_trilha_hora = float(input('Informe o tempo de duração da trilha(horas): '))

print(f'Sua média de velocidade durante essa trilha foi de {velocidade_media(distancia_percorrida_km,tempo_trilha_hora):.2f} km/h.')

