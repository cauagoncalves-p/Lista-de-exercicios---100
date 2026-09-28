# Exercício 27 - Classificação de IMC
# Leia o peso (kg) e a altura (m), calcule o IMC e classifique:
# IMC = peso / (altura x altura)
# < 18,5              -> ABAIXO DA FAIXA
# 18,5 a < 25,0        -> FAIXA NORMAL
# 25,0 a < 30,0        -> ACIMA DA FAIXA
# >= 30,0              -> FAIXA ELEVADA

def exercicio_27():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "ABAIXO DA FAIXA"
    elif imc < 25.0:
        classificacao = "FAIXA NORMAL"
    elif imc < 30.0:
        classificacao = "ACIMA DA FAIXA"
    else:
        classificacao = "FAIXA ELEVADA"

    print(f"IMC: {imc:.1f}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    exercicio_27()
