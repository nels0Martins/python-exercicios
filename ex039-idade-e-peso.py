print()

peso90 = 0
soma_id = 0

for p in range(3):
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso: "))

    if peso > 90.0:
        peso90+=1

    soma_id+=idade
    media = float(soma_id/3)

print()

print(f"Quantidade de pessoas com mais de 90Kg's: {peso90}")
print(f"Média das idades digitadas: {media :.1f}")

print()