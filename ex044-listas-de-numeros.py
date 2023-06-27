print()

somando = 0
valores = []
# Lista vazia 

for n in range(5): # Criando estrutura de repetição para rodar 5 vezes
   numero = int(input("Digite um valor: "))
   valores.append(numero) # Adicionando os elementos dentro da lista

print()

print(f"Os valores são: {valores}")
print(f"Quantidade de elementos que tem na lista: {len(valores)}") # len() é uma função que conta quantos valores tem na lista!

#for v in valores: 
# A cada repetição ele vai acessar a lista 'valores' acessar um elemento e guardar na variavel 'v'
    #somando+=v # Somador

for i in range(len(valores)): 
   somando+=valores[i] # somando os valores de acordo com a contagem da lista

print(f"Somatorio de todos os itens da lista: {somando}")

print()