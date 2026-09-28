# Exercício 28 - É possível formar um triângulo?
# Leia três medidas positivas e informe se elas podem formar um triângulo.
# Regra: cada lado deve ser menor que a soma dos outros dois.

def exercicio_28():
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))

    if a < b + c and b < a + c and c < a + b:
        print("Resultado: FORMAM UM TRIÂNGULO")
    else:
        print("Resultado: NÃO FORMAM UM TRIÂNGULO")


if __name__ == "__main__":
    exercicio_28()
