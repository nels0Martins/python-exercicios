
while True:
    valor_km = 0.75
    print("Quantos Km da Lovely Pet até a casa do pet?")
    distancia_km = float(input())
    ida_e_volta = distancia_km * 2

    if ida_e_volta >= 3:
        total = (ida_e_volta * valor_km)
        print(
            "Valor a cobrar do cliente pela viagem inteira R${:.2f}!".format(total))

    elif distancia_km <= 3:
        print("Valor a cobrar do cliente pela viagem inteira: R$5,00!\n")
