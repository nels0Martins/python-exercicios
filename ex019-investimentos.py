print()
print("=-"*30, "Investimentos", "=-"*30)
print('''Poupança [1]
Renda fixa [2]''')
print()
num = int(input("Digite o número do investimento que você deseja: "))

if num == 1:
    valor = float(input("Digite o valor do investimento: "))
    correcao = valor + (valor*3/100)
    print(f"Valor corrigido com um rendimento de 3% no último mês: {correcao}")
elif num == 2:
    valor = float(input("Digite o valor do investimento: "))
    correcao = valor + (valor*4/100)
    print(f"Valor corrigido com um rendimento de 4% no último mês: R${correcao :.2f}")
else:
    print("Número inválido!")
print()
