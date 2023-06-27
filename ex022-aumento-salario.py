print()
sal = float(input("Digite seu salário: "))

if sal <= 300:
    aumento = sal + (sal*35/100)
    print("Você recebeu um aumento de 35% o seu salário agora é de R${aumento :.2f}")
if sal > 300:
    aumento = sal + (sal*15/100)
    print("Você recebeu um aumento de 15% o seu salário agora é de R${aumento :.2f}")
    
