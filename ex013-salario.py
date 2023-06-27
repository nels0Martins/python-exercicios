print()
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))
horas_extras = float(input("Digite o número de horas extras trabalhadas: "))

valor_ht = salario_minimo/8
valor_he = salario_minimo/4

bruto = horas_trabalhadas*valor_ht
bruto_he = horas_extras*valor_he

sal_final = bruto + bruto_he

print()
print(f"O salário a receber é de R${sal_final :.2f}!")
print()