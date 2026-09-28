# Exercício 19 - Maior e menor de três números
# Leia três números reais e mostre o maior e o menor valor informado.
# Requisito: o programa deve funcionar também quando houver valores repetidos.


entrada = input("Valores (separados por vírgula): ")
valores = [float(x.strip()) for x in entrada.split(",")]

maior = valores[0]
menor = valores[0]
for v in valores[1:]:
    if v > maior:
        maior = v
    if v < menor:
        menor = v

print(f"Maior: {maior}")
print(f"Menor: {menor}")


