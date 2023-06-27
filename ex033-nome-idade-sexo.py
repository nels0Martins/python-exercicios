cont_m = 0

for pessoas in range(20):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite seu sexo (F ou M): ").upper()
      
    if sexo == 'M' and idade > 21:
        cont_m+=1

print(f"Existem {cont_m} pessoas do sexo masculino e possuem mais de 21 anos!")
