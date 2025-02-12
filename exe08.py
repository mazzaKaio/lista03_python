# Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

excessoVelocidade = 80
velocidadeCarro = float(input("Digite a velocidade em que se encontrava o carro: "))

if velocidadeCarro > excessoVelocidade:

    diferencaVelocidade = velocidadeCarro - excessoVelocidade
    valorMulta = 5 * diferencaVelocidade
    print("Você será multado em R$", valorMulta, " por excesso de velocidade!")
else:
    print("Tudo normal por aqui, tenha um ótimo dia!")