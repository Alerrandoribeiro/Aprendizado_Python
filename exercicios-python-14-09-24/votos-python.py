""" 4 - Uma cidade pretende apurar os votos de sua eleição. Faça um programa para ler o número total de eleitores. Em seguida o número de votos do candidato X, o número de votos do candidato Y, total de votos brancos e total de votos nulos (a soma desses quatro, deve ser igual ao total de eleitores). Calcular e escrever o percentual que cada um representa em relação ao total de eleitores. """

percentual = 100;

numeroTotalEleitores = int(input('Informe o total de eleitores: '));
numeroDeVotosCandidatoX = int(input('Informe o número de votos do candidato X: '));
numeroDeVotosCandidatoY = int(input('Informe o número de votos do candidato Y: '));
totalVotosBrancos = int(input('Informe o total de votos brancos: '));
totalVotosNulos = int(input('Informe o total de votos nulos: '));

mediaCandidatoX = (numeroTotalEleitores * numeroDeVotosCandidatoX) / percentual
mediaCandidatoY = (numeroTotalEleitores * numeroDeVotosCandidatoY) / percentual
mediaVotosBrancos = (numeroTotalEleitores * totalVotosBrancos) / percentual
mediaVotosNulos = (numeroTotalEleitores * totalVotosNulos) / percentual 

print(f'Total de eleitores: {numeroTotalEleitores} eleitores\nNúmero de votos Candidato X: {numeroDeVotosCandidatoX} eleitores e representa {mediaCandidatoX}% dos votos\nNúmero de votos Candidato Y: {numeroDeVotosCandidatoY} eleitores e representa {mediaCandidatoY}% dos votos\nTotal de votos brancos: {totalVotosBrancos} eleitores que representa {mediaVotosBrancos} % dos votos\nTotal votos nulos: {totalVotosNulos} eleitores que representa {mediaVotosNulos} % dos votos');