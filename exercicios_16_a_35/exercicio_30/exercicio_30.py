# Exercício 30 - Aprovação de empréstimo
# Leia o valor de um imóvel, o salário mensal do comprador e o prazo em anos.
# Calcule a prestação mensal e informe se o empréstimo foi aprovado.
# Prestação = valor do imóvel / (anos x 12)
# Aprovado quando a prestação não ultrapassa 30% do salário.

def exercicio_30():
    imovel = float(input("Valor do imóvel: "))
    salario = float(input("Salário: "))
    anos = int(input("Prazo (anos): "))

    prestacao = imovel / (anos * 12)
    limite = salario * 0.30
    resultado = "APROVADO" if prestacao <= limite else "NEGADO"

    print(f"Prestação: R$ {prestacao:.2f}")
    print(f"Limite: R$ {limite:.2f}")
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    exercicio_30()
