print()

total_avista = 0.0
total_aprazo = 0.0
primeira_parcela = 0.0

print("Escolha seu tipo de transação:")
print('''A Vista - [V]
A Prazo - [P]''')

print()

for num in range(3):
    codigo = str(input("Digite o código da transação (V/P): ")).upper()
    valor = float(input("Digite o valor da transação: "))
    print()

    if codigo == 'V':
        total_avista+=valor

    if codigo == 'P':
        total_aprazo+=valor 
        div = int(input("Digite em quantas parcelas você deseja dividir (1 a 3x): ")) 
        prestacao = valor/div
        primeira_parcela+=prestacao

        print()

    total_compras = total_avista + total_aprazo

print()

print(f'''a) Total de compras a vista: R${total_avista :.2f}
b) Total de compras a prazo: R${total_aprazo :.2f} 
c) Total de compras efetuadas: R${total_compras :.2f}
d) Valor da primeira parcela das compras a prazo (juntas): R${primeira_parcela :.2f}''')

print()

    
    

