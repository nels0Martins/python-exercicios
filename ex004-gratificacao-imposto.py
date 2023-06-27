print()
sal = float(input("Digite o seu salário base: "))
g = sal*5/100
ir = sal*7/100
salf = sal + g - ir
print()
print(f'''= Salário bruto: R${sal :.2f}
+ Gratificação: R${g :.2f}
- Imposto de renda: R${ir :.2f}
= Salário líquido: R${salf :.2f}
''')
print()