# Exercício 25 - Preço conforme a forma de pagamento
# Leia o preço de um produto e a opção de pagamento e calcule o valor final:
# 1 - Dinheiro ou Pix     -> 10% de desconto
# 2 - Débito              -> 5% de desconto
# 3 - Crédito à vista     -> sem alteração
# 4 - Crédito parcelado   -> 8% de acréscimo

def exercicio_25():
    preco = float(input("Preço: "))
    opcao = int(input("Opção: "))

    if opcao == 1:
        valor_final = preco * 0.90
    elif opcao == 2:
        valor_final = preco * 0.95
    elif opcao == 3:
        valor_final = preco
    elif opcao == 4:
        valor_final = preco * 1.08
    else:
        print("Opção inválida")
        return

    print(f"Valor final: R$ {valor_final:.2f}")


if __name__ == "__main__":
    exercicio_25()
