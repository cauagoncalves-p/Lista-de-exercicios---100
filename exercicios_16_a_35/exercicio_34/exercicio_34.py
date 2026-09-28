# Exercício 34 - Quantidade de dias do mês
# Leia o número de um mês e um ano. Mostre quantos dias o mês possui.
# Meses 1,3,5,7,8,10,12 -> 31 dias | Meses 4,6,9,11 -> 30 dias
# Fevereiro -> 28 dias, ou 29 em ano bissexto
# Se o mês estiver fora de 1 a 12, mostre MÊS INVÁLIDO.

def exercicio_34():
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))

    if mes < 1 or mes > 12:
        print("MÊS INVÁLIDO")
        return

    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias = 31
    elif mes in (4, 6, 9, 11):
        dias = 30
    else:  # fevereiro
        bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
        dias = 29 if bissexto else 28

    print(f"{dias} dias")


if __name__ == "__main__":
    exercicio_34()
