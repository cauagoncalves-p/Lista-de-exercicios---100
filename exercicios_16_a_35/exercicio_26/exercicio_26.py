# Exercício 26 - Reajuste por faixa salarial
# Leia o salário atual e calcule o novo salário conforme a tabela:
# até R$ 1.500,00                 -> 15%
# de R$ 1.500,01 até R$ 3.000,00  -> 10%
# acima de R$ 3.000,00            -> 5%

def exercicio_26():
    salario = float(input("Salário atual: "))

    if salario <= 1500:
        percentual = 0.15
    elif salario <= 3000:
        percentual = 0.10
    else:
        percentual = 0.05

    aumento = salario * percentual
    novo_salario = salario + aumento

    print(f"Percentual: {percentual * 100:.0f}%")
    print(f"Aumento: R$ {aumento:.2f}")
    print(f"Novo salário: R$ {novo_salario:.2f}")


if __name__ == "__main__":
    exercicio_26()
