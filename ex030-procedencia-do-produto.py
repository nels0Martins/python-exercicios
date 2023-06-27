print()
codigo = int(input("Digite o código para verificarmos a origem do produto: "))

if codigo == 1:
    print("Origem: Sul!")
elif codigo == 2:
    print("Origem: Norte!")
elif codigo == 3:
    print("Origem: Leste")
elif codigo == 4:
    print("Origem: Oeste")
elif codigo == 5 or codigo == 6:
    print("Origem: Nordeste")
elif codigo >= 7 and codigo <= 9:
    print("Origem: Sudeste")
elif codigo >= 10 and codigo <= 20:
    print("Origem: Centro-oeste")
else:
    print("Código sem origem ou inválido!")

print()
