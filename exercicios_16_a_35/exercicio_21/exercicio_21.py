# Exercício 21 - Aprovado ou reprovado
# Leia duas notas, calcule a média e informe se o aluno foi aprovado ou reprovado.
# Regra: média >= 7,0 -> APROVADO; abaixo de 7,0 -> REPROVADO.


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2

situacao = "APROVADO" if media >= 7.0 else "REPROVADO"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")

