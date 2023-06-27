print()

numeros = [10, True, 5.0, 'a', [0,1]] 
# Podemos colocar vários tipos de valores na lista inclusive outra lista
# Porem a recomendação é sempre criar uma lista para cada tipo de dado

lista = [] # Lista vazia

print(numeros[4][0:2]) 
# Imprimindo o primeiro valor da lista 'numeros', a contagem da lista começa no valor 0. 

print()

numeros.append(8) # Adicionando o valor 8 na lista numeros
numeros.append(60)

print(numeros[-1]) # -1 sempre é ultimo valor da lista

print()

numeros[1] = False # Editando a posição 1 da lista!

print(numeros[1])

print()