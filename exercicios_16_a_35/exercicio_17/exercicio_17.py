# Exercício 17 - Par ou ímpar
# Leia um número inteiro e informe se ele é par ou ímpar.
# Regra: um número é par quando o resto da divisão por 2 é igual a zero.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = "PAR"
else:
    resultado = "ÍMPAR"

print(f"Resultado: {resultado}")
