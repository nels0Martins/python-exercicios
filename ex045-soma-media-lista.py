print()

lista = [] # Lista vazia
soma = 0 # Somatorio
media = 0 # Media

for i in range(6): # Repetir 'i' cinco vezes (i = 0)
    num = int(input("Digite os números: ")) # Entrada de numeros
    lista.append(num) # Guarda os números na lista
    soma = soma + num #soma+=num
    media = soma/len(lista) 

print()
print(f"Lista: {lista}")
print(f"Soma do números: {soma}")
print(f"Média dos números: {media}")

print()