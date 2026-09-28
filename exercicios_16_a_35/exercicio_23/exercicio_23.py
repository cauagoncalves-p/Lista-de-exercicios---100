# Exercício 23 - Categoria de votação
# Leia a idade de uma pessoa e informe a categoria de votação:
# menor de 16          -> NÃO PODE VOTAR
# 16 ou 17             -> VOTO OPCIONAL
# 18 a 69              -> VOTO OBRIGATÓRIO
# 70 ou mais           -> VOTO OPCIONAL

def exercicio_23():
    idade = int(input("Idade: "))

    if idade < 16:
        categoria = "NÃO PODE VOTAR"
    elif idade <= 17:
        categoria = "VOTO OPCIONAL"
    elif idade <= 69:
        categoria = "VOTO OBRIGATÓRIO"
    else:
        categoria = "VOTO OPCIONAL"

    print(f"Categoria: {categoria}")


if __name__ == "__main__":
    exercicio_23()
