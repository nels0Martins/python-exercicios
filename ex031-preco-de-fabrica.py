'''
preco = custo_fabrica (soma + distribuidor + impostos)

'''
print()
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

if custo_fabrica <= 12000:
    preco = custo_fabrica + (5*custo_fabrica/100)
    print(f"Preço do carro: R${preco :.2f}")

elif custo_fabrica >= 12000 and custo_fabrica <= 25000:
    preco = custo_fabrica + ((10*custo_fabrica/100) + (15*custo_fabrica/100))
    print(f"Preço do carro: R${preco :.2f}")
    
elif custo_fabrica > 25000:
    preco = custo_fabrica + ((15*custo_fabrica/100) + (20*custo_fabrica/100))
    print(f"Preço do carro: R${preco :.2f}")

print()