print()
idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria: Infantil")
elif idade >= 8 and idade <= 10:
    print("Categoria: Juvenil")
elif idade >= 11 and idade <= 15:
    print("Categoria: Adolescente")
elif idade >= 16 and idade <= 30:
    print("Categoria: Adulto")
elif idade > 30:
    print("Categoria: Senior")
else: 
    print("Você é muito jovem para praticar natação!")

print()