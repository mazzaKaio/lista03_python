# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite seu salário: "))

if salario <= 1250:
    aumento = 0.15
else:
    aumento = 0.10

salarioPromocao = salario + (salario * aumento)

print("Seu salário pós-aumento será de:", salarioPromocao)
print("'Kaio Gomes do Nascimento Mazza'")