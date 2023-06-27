print("=-"*10, "Peso ideal!!", "=-"*10)
print("Você é homem ou mulher?")
s = input("Digite H ou M: ")

if s == 'h' or s == 'H':
    print()
    p = float(input("Digite seu peso: "))
    al = float(input("Digite a sua altura: "))
    ideal = (72.7*al) - 58
    print(f"Seu peso ideal é de {ideal :.2f}Kg's")
    
if s == 'm' or s == 'M':
    print()
    p = float(input("Digite seu peso: "))
    al = float(input("Digite a sua altura: "))
    ideal = (62.1*al) - 44.7
    print(f"Seu peso ideal é de {ideal :.2f}Kg's")
