print()

reprovados = 0
recuperacao = 0
aprovados = 0
total_medias = 0.0

for num in range(3):
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    media = (n1+n2)/2
    print()

    print(f"Média: {media :.1f}")
    total_medias+=media

    if media <= 3:
        print("Resultado: Reprovado!")
        reprovados+=1
        print()
    
    elif media >= 3 and media < 7:
        print("Resultado: Recuperação!")
        recuperacao+=1
        print()

    elif media > 7:
        print("Resultado: Aprovado!")
        aprovados+=1
        print()

    media_classe = total_medias/6 

print()

print(f"Total de alunos reprovados: {reprovados}\nTotal de alunos em recuperação: {recuperacao}\nTotal de alunos aprovados: {aprovados}")
print(f"Média da classe: {media_classe :.1f}")

print()