print()

def somar(n1, n2): # Função somar com dois parametros
    soma = n1+n2 # Depois da entrada de parametros a função os soma e guarda na variavel "soma"
    return soma # Apos isso a função retorna soma

n1 = int(input("Digite um número: ")) # Entradas
n2 = int(input("Digite outro: "))
soma = somar(n1, n2) # Variavel soma que guarda o retorno da soma

print(f"{n1} + {n2} = {soma}") # Exibindo

print()