# Exercício 20 - Três valores em ordem crescente
# Leia três números inteiros e mostre os valores em ordem crescente.
# Requisito: aceite valores repetidos.


entrada = input("Valores (separados por vírgula): ")
valores = [int(x.strip()) for x in entrada.split(",")]

    # ordenação simples (bolha) para praticar a lógica manualmente
for i in range(len(valores)):
    for j in range(len(valores) - 1 - i):
        if valores[j] > valores[j + 1]:
            valores[j], valores[j + 1] = valores[j + 1], valores[j]

print("Ordem crescente:", ", ".join(str(v) for v in valores))


if __name__ == "__main__":
    exercicio_20()
