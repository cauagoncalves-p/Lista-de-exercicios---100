# Exercício 24 - Ano bissexto
# Leia um ano inteiro e informe se ele é bissexto.
# Regra: divisível por 400, ou divisível por 4 e não divisível por 100.

def exercicio_24():
    ano = int(input("Ano: "))

    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)

    print("Resultado: ANO BISSEXTO" if bissexto else "Resultado: NÃO BISSEXTO")


if __name__ == "__main__":
    exercicio_24()
