# Exercício 35 - Valor do ingresso
# O ingresso custa R$ 30,00. Leia a idade e informe se a pessoa é estudante.
# Calcule o valor final: paga meia-entrada (50%, não acumulativo) quem tiver
# menos de 12 anos, quem for estudante, ou quem tiver 60 anos ou mais.

def exercicio_35():
    preco_cheio = 30.0
    idade = int(input("Idade: "))
    estudante = input("Estudante (S/N): ").strip().upper() == "S"

    meia_entrada = idade < 12 or estudante or idade >= 60
    valor = preco_cheio * 0.5 if meia_entrada else preco_cheio

    print(f"Valor do ingresso: R$ {valor:.2f}")


if __name__ == "__main__":
    exercicio_35()
