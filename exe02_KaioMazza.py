# Peça ao usuário para inserir um número inferior a 20. Se ele inserir um número 20 ou mais, 
# exiba a mensagem "Muito alto", caso contrário, exiba "Obrigado".

num = float(input("Digite um número inferior a 20:"))
if num >= 20:
    print("Número inserido MUITO ALTO!")
else:
    print("Obrigado!")
print("'Kaio Gomes do Nascimento Mazza'")