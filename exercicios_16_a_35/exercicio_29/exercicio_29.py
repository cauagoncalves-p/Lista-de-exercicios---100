# Exercício 29 - Tipo de triângulo
# Leia três medidas. Primeiro verifique se elas formam um triângulo.
# Se formarem, classifique como equilátero, isósceles ou escaleno.

def exercicio_29():
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))

    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            tipo = "EQUILÁTERO"
        elif a == b or a == c or b == c:
            tipo = "ISÓSCELES"
        else:
            tipo = "ESCALENO"
        print(f"Resultado: {tipo}")
    else:
        print("Resultado: NÃO FORMA TRIÂNGULO")


if __name__ == "__main__":
    exercicio_29()
