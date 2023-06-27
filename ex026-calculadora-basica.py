print("=" * 27, "Calculadora Básica", "=" * 27)
print()

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print()

print('''Qual operacação você deseja?
Adição [1]
Subtração [2]
Multiplicação [3]
Divisão [4]
''')
operacao = int(input("Digite o número da operação: "))
print()

if operacao == 1:
  s = n1+n2
  print(f"{n2} + {n2} = {s}")

elif operacao == 2:
  sub = n1-n2 
  print(f"{n1} - {n2} = {sub}")

elif operacao == 3:
  m = n1*n2
  print(f"{n1} x {n2} = {m}")

elif operacao == 4:
  if n2 != 0:
    d = n1/n2
    print(f"{n1} / {n2} = {d}")

  else:
    print("Não é possivel dividir {n1} por zero!")
