print()
ht = float(input("Digite o número de horas trabalhadas: "))
salmin = float(input("Digite o valor do salário minímo: "))
valor_ht = salmin/2
salbruto = valor_ht*ht
ir = salbruto*3/100
salrecebe = salbruto - ir
print(f"Salário a receber: R${salrecebe :.2f}!")
print()