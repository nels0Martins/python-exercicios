print()

def par_ou_impar(n):
    if n % 2 == 0:
        r = 'PAR'
    else:
        r = 'IMPAR'
    return r

n = int(input("Digite um número: "))
r = par_ou_impar(n)

print(f"O número {n} é {r}!")

print()