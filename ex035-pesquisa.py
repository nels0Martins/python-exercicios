print()

somador_sal = 0.0
media_sal = 0.0
qtd_sal = 0
maior_idade = 0
menor_idade = 0
cont_f = 0

while True:
    idade = int(input("Digite a sua idade: "))

    if qtd_sal == 0:
        maior_idade = idade
        menor_idade = idade

    if idade < 0:
        break
    
    sexo = input("Digite o sexo (M/F): ").upper()
    sal = float(input("Digite o seu salário: "))

    somador_sal+=sal  
    if sal > 0:
        qtd_sal+=1     
    media_sal = somador_sal/qtd_sal

    if idade > maior_idade:
        maior_idade = idade
        
    if idade < menor_idade:
        menor_idade = idade

    if sexo == 'F' and sal > 200.0:
        cont_f+=1 

print(f'''a) Quantidade de salários digitados: {qtd_sal}
b) Maior idade {maior_idade} e Menor idade {menor_idade}
c) Quantidade de mulheres com salário maior que R$200,00: {cont_f
}
''')
    
