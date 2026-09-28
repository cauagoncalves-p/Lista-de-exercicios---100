# Exercício 18 - Maior de dois números
# Leia dois números reais e mostre qual deles é o maior.
# Se os valores forem iguais, informe que não existe maior.

v1 = float(input("Primeiro valor: "))
v2 = float(input("Segundo valor: "))

if v1 > v2:
    print(f"Maior valor: {v1}")
elif v2 > v1:
    print(f"Maior valor: {v2}")
else:
    print("VALORES IGUAIS")
