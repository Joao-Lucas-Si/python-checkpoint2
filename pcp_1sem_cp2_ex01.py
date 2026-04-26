#  Gabriel

estado = int(input("Digite o código do estado de origem da carga (1 a 5): "))
peso_ton = float(input("Digite o peso da carga (TONELADAS): "))
codigo_carga = int(input("Digite o código da carga (10 a 40)"))


peso_kg = peso_ton * 1000

if 10 <= codigo_carga <= 20:
    preco_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_kg = 250
else:
    preco_kg = 340


preco_carga = peso_kg * preco_kg

if estado == 1:
    imposto = preco_carga * 0.35
elif estado == 2:
    imposto = preco_carga * 0.25
elif estado == 3:
    imposto = preco_carga * 0.15
elif estado == 4:
    imposto = preco_carga * 0.05
else:
    imposto = 0
    
total = preco_carga + imposto

print("\n---Resultados---")
print(f"Peso da carga: {peso_kg:.2f} Kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"valor total: R$ {total:.2f}")