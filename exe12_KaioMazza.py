# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). 
# Exiba o resultado da operação solicitada. (usar ELIF)

num1 = float(input("Digite o primeiro número: "))
operacao = str(input("Digite qual operação você deseja usar (+), (-), (*), (/): "))
num2 = float(input("Digite o segundo número: "))

if operacao.__eq__("+"):
    resultado = num1 + num2
    print(num1, "+", num2, "=", resultado)

elif operacao.__eq__("-"):
    resultado = num1 - num2
    print(num1, "-", num2, "=", resultado)

elif operacao.__eq__("*"):
    resultado = num1 * num2
    print(num1, "*", num2, "=", resultado)

elif operacao.__eq__("/"):
    resultado = num1 / num2
    print(num1, "/", num2, "=", resultado)

else:
    print("Operação não aceita!")
print("'Kaio Gomes do Nascimento Mazza'")