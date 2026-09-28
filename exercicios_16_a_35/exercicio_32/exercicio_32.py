# Exercício 32 - Número dentro do intervalo
# Leia um número real e informe se ele está dentro do intervalo fechado
# de 10 até 20 (os valores 10 e 20 pertencem ao intervalo).

def exercicio_32():
    n = float(input("Digite um número: "))

    print("Resultado: DENTRO" if 10 <= n <= 20 else "Resultado: FORA")


if __name__ == "__main__":
    exercicio_32()
