print()

def contagem(n1, n2):
    numeros = []
    for cont in range(n1, n2+1):
        numeros.append(cont)
    return numeros
    
n1 = int(input("De onde iremos contar: "))
n2 = int(input("Até onde iremos contar: "))
cont = contagem(n1, n2)

print(cont,"\n")


print()