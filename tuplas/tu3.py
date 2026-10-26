print("3. TUPLAS SÃO IMUTÁVEIS:\n")

tupla = (1, 2, 3)
print(f"Tupla original: {tupla}\n")

print("Tentando modificar:")
try:
    tupla[0] = 99
except TypeError as e:
    print(f"❌ Erro: {e}\n")

print("Tentando adicionar:")
try:
    tupla.append(4)
except AttributeError as e:
    print(f"❌ Erro: Tuplas não têm append\n")

print("✓ Tuplas são imutáveis (proteção de dados)")
print("✓ Listas podem ser modificadas\n")

print("="*60 + "\n")