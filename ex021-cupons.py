print()
venda = float(input("Digite o valor da venda: "))

if venda >= 20:
    cupons = int(venda/20)
    print(f"Você tem direito a {cupons} cupom(s)!")
else:
    print("Você não tem direito a cupons!!")
