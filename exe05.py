# Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite. 
# Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva", 
# caso contrário, exiba a mensagem "Pegue um guarda-chuva". Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".

estaChovendo = input("Está chovendo hoje? Insira sua resposta: ")

if estaChovendo.lower().__eq__("sim"):
    estaVentando = input("Está ventando hoje? Insira sua resposta: ")

    if estaVentando.lower().__eq__("sim"):
        print("\nEstá ventando muito para um guarda-chuva!")
    else:
        print("\nPegue um guarda-chuva!")
else:
    print("\nEntão, aproveite seu dia!")