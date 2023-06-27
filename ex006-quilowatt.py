print()
salmin = float(input("Digite o valor do salário minímo: "))
qtd_qw = float(input("Quantos quilowatts foram consumidos pela residência: "))
qw = salmin/5
total = qtd_qw*qw
desconto = total - (total*15/100)
print()
print(f"O valor de cada Quilowatt é de R${qw :.2f}")
print(f"O valor a ser pago pela residência é de R${total :.2f}")
print(f"Com um desconto de 15% o valor a ser pago pela residência é de R${desconto :.2f}!")
print()