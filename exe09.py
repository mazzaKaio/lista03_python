# Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.

rendaMensal = float(input("Digite sua renda mensal (R$): "))

if rendaMensal <= 2259.20:
    print("Aliquota nula!")
else:
    if rendaMensal >= 2259.21 and rendaMensal <= 2826.65:
        aliquota = 0.075
        imposto = rendaMensal * aliquota
        print("Seu imposto conforme a tabela de 2025 é: R$", imposto)
    else:
        if rendaMensal >= 2826.66 and rendaMensal <= 3751.05:
            aliquota = 0.15
            imposto = rendaMensal * aliquota
            print("Seu imposto conforme a tabela de 2025 é: R$", imposto)
        else:
            if rendaMensal >= 3751.06 and rendaMensal <= 4664.68:
                aliquota = 0.225
                imposto = rendaMensal * aliquota
                print("Seu imposto conforme a tabela de 2025 é: R$", imposto)
            else:
                if rendaMensal >= 4664.68:
                    aliquota = 0.275
                    imposto = rendaMensal * aliquota
                    print("Seu imposto conforme a tabela de 2025 é: R$", imposto)
print("'Kaio Gomes do Nascimento Mazza'")