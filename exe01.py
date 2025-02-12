# Peça dois números. Se o primeiro for maior que o segundo, exiba primeiro o segundo número e depois o primeiro número, 
# caso contrário, mostre primeiro o  número e depois o segundo.

num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite mais um número inteiro:"))

if num1 > num2:
    print("\nSegundo número:", num2, "\nPrimeiro número:", num1)
else:
    print("\nPrimeiro número:", num1, "\nSegundo número:", num2)
print("'Kaio Gomes do Nascimento Mazza'")