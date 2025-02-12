# Pergunte a idade do usuário. Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar", 
# se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir", 
# se tiver 14 anos, exiba a mensagem "Você pode comprar um bilhete de loteria", 
# se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras".

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode aprender a dirigir!")
else:
    if idade >= 16:
        print("Você pode votar!")
    else:
        if idade == 14 or idade == 15:
            print("Você pode comprar um bilhete de loteria!")
        else:
            print("Você pode fazer doces ou travessuras!")
print("'Kaio Gomes do Nascimento Mazza'")