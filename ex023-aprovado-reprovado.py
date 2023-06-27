print()
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite a sua segunda nota: "))
media = (n1+n2)/2

if media >= 7:
    print()
    print(f"MÉDIA: {media :.1f}")
    print("APROVADO!")
elif media < 7:
    print()
    print(f"MÉDIA: {media :.1f}")
    print("REPROVADO!")
