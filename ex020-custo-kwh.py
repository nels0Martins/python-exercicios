print()

print('''Tipo de instalação:
Residências: [R]
Indústrias: [I]
Comércios: [C]
''')

tipo_instalacao = input("Digite o tipo de instalação (R, I ou C): ").upper()

if tipo_instalacao == 'R':

    kwh = float(input("Digite a quantidade de KWH: "))

    if kwh <= 500:
        preco = kwh*0.40
        print(f"Total a pagar R${preco :.2f}")
        
    elif kwh > 500:
        preco = kwh*0.65
        print(f"Total a pagar R${preco :.2f}")

    
elif tipo_instalacao == 'I':

    kwh = float(input("Digite a quantidade de KWH: "))

    if kwh <= 5000:
        preco = kwh*0.55
        print(f"Total a pagar R${preco :.2f}")
        
    elif kwh > 5000:
        preco = kwh*0.60
        60
        print(f"Total a pagar R${preco :.2f}")

elif tipo_instalacao == 'C':

    kwh = float(input("Digite a quantidade de KWH: "))

    if kwh <= 1000:
        preco = kwh*0.55
        print(f"Total a pagar R${preco :.2f}")
        
    elif kwh > 1000:
        preco = kwh*0.60
        print(f"Total a pagar R${preco :.2f}")
   
    
    
