print() 

def dobro(n1): # Função chamada dobro que recebe um valor
    dobro = n1*2 # Ao receber esse valor a variavel dobro faz o valor * 2
    return dobro # E retorna esse valor de dobro

a = int(input("Digite um número: ")) # Aqui o número entra
r = dobro(a) # Aqui o retorno de dobro é guardado na variavel r

print(f"O dobro de {a} é {r}") # Exibindo

print()