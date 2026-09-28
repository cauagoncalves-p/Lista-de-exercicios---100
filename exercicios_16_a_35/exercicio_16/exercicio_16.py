# Exercício 16 - Positivo, negativo ou zero
# Leia um número real e informe se ele é positivo, negativo ou igual a zero.

def exercicio_16():
    valor = float(input("Digite um número: "))

    if valor > 0:
        resultado = "POSITIVO"
    elif valor < 0:
        resultado = "NEGATIVO"
    else:
        resultado = "ZERO"

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    exercicio_16()
