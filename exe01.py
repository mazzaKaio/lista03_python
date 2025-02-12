# Peça dois números, se o PRIMERIO NÚMERO for MAIOR que o SEGUNDO, exiba primerio o SEGUNDO NÚMERO
# caso contrário, exiba o PRIMEIOR NÚMERO e depois o SEGUNDO

num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite mais um número inteiro:"))

if num1 > num2:
    print("\nSegundo número:", num2, "\nPrimeiro número:", num1)
else:
    print("\nPrimeiro número:", num1, "\nSegundo número:", num2)