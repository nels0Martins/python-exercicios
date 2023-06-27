print()

lista = []
listapar = []
listaimpar = []

for i in range(6):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        listapar.append(num)
    
    else:
        listaimpar.append(num)

print()

print(f"Lista de números pares: {listapar}")
print(f"Lista de números impares: {listaimpar}")
print()
print(f"Quantidade de números pares: {len(listapar)}")
print(f"Quantidade de números ímpares: {len(listaimpar)}")

print()