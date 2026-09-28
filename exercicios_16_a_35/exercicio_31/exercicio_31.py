# Exercício 31 - Divisível por 3 e por 5
# Leia um número inteiro e informe em qual situação ele se encontra:
# divisível por 3 e por 5, apenas por 3, apenas por 5, ou por nenhum dos dois.

def exercicio_31():
    n = int(input("Digite um número: "))
    div3 = n % 3 == 0
    div5 = n % 5 == 0

    if div3 and div5:
        print("Saída: DIVISÍVEL POR 3 E 5")
    elif div3:
        print("Saída: DIVISÍVEL APENAS POR 3")
    elif div5:
        print("Saída: DIVISÍVEL APENAS POR 5")
    else:
        print("Saída: NÃO DIVISÍVEL POR 3 NEM 5")


if __name__ == "__main__":
    exercicio_31()
