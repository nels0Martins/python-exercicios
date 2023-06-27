print()

def soma(n1, n2):
    s = n1+n2
    return s

def subtracao(n1, n2):
    sub = n1-n2
    return sub

def multiplicacao(n1, n2):
    multi = n1*n2
    return multi

def divisao(n1, n2):
    if n2 != 0:
        div = n1/n2
        return div
    else:
        msg = "Não posso dividir números por 0!"
        return msg

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro: "))

print()

print('''Menu:
1 - SOMA
2 - SUBTRACAO
3 - MULTI
4 - DIV''')

print()
 
codigo = int(input("Código: "))

print()

if codigo == 1:
    calc = soma(n1,n2)
    print(f"{n1} + {n2} = {calc}")

elif codigo == 2:
    calc = subtracao(n1,n2)
    print(f"{n1} - {n2} = {calc}")

elif codigo == 3:
    calc = multiplicacao(n1,n2)
    print(f"{n1} x {n2} = {calc}")

elif codigo == 4:
    calc = divisao(n1,n2)
    print(f"{n1} / {n2} = {calc}")

else:
    print("ERRO")

print()