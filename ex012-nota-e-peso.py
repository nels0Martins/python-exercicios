print()
n1 = float(input("Digite a sua primeira nota: "))
p1 = float(input("Agora digite o peso dessa nota: "))
n2 = float(input("Digite a sua segunda nota: "))
p2 = float(input("Agora digite o peso dessa nota: "))
n3 = float(input("Digite a sua terceira nota: "))
p3 = float(input("Agora digite o peso dessa nota: "))
mp = (n1*p1 + n2*p2 + n3*p3) / (p1+p2+p3)
print()
print(f"A média ponderada é de {mp :.1f}!")
print()