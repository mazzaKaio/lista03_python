# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distanciaDesejada = float(input("Insira o quando (em KM) você deseja percorrer:"))

if distanciaDesejada < 200:
    precoPassagem = distanciaDesejada * 0.5
else:
    precoPassagem = distanciaDesejada * 0.45

print("Sua viagem irá custar: R$", precoPassagem)
print("'Kaio Gomes do Nascimento Mazza'")