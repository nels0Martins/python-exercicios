print()

he = float(input("Digite o número de horas extras trabalhadas: "))
hf = float(input("Digite o número de horas de trabalho perdidas: "))

h = he - ((2/3) * hf)

if h > 2400:
    print("Gratificação: R$500,00")

elif h >= 1800 and h <= 2400:
    print("Gratificação R$400,00")

elif h >= 1200 and h <= 1800:
    print("Gratificação R$300,00")

elif h >= 600 and h <= 1200:
    print("Gratificação R$200,00")

elif h < 600:
    print("Gratificação R$100,00")

print()