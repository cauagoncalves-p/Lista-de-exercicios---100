# Exercício 22 - Situação do aluno por faixa
# Leia duas notas, calcule a média e informe a situação conforme a tabela:
# média < 5,0            -> REPROVADO
# 5,0 <= média < 7,0     -> RECUPERAÇÃO
# média >= 7,0           -> APROVADO


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2

if media < 5.0:
    situacao = "REPROVADO"
elif media < 7.0:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")

