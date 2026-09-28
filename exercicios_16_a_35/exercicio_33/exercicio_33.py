# Exercício 33 - Dia da semana
# Leia um número de 1 a 7 e mostre o dia da semana correspondente.
# Para qualquer outro valor, mostre OPÇÃO INVÁLIDA.

def exercicio_33():
    dias = {
        1: "SEGUNDA-FEIRA",
        2: "TERÇA-FEIRA",
        3: "QUARTA-FEIRA",
        4: "QUINTA-FEIRA",
        5: "SEXTA-FEIRA",
        6: "SÁBADO",
        7: "DOMINGO",
    }

    numero = int(input("Número (1 a 7): "))
    print(dias.get(numero, "OPÇÃO INVÁLIDA"))


if __name__ == "__main__":
    exercicio_33()
