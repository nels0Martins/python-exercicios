# Importações:
from time import sleep

# Início:
print("\n","*"*15, "CONTROLE BANCÁRIO", "*"*15,"\n")

# Listas e contadores:
codigos_lista = []
saldos_lista = []
cont = 0

print("CADASTR0 DE CONTAS:")

# Looping para entradas:
while len(codigos_lista) + len(saldos_lista) < 20: 
    codigo = int(input(f"\nDigite o código da {cont+1}° conta: "))   
    # Adicionando itens a lista e pedindo recebendo saldo a depender da condição:
    if codigo not in codigos_lista:
        saldo = float(input(f"Digite o saldo {cont+1}° conta: "))
        codigos_lista.append(codigo)
        saldos_lista.append(saldo)
        cont+=1 # Contador

    # Mensagem de erro: 
    else:
        print("\n","="*10, f"ERRO: Código '{codigo}' já foi cadastrado!", "="*10)

# Váriavel para as operações do menu: 
operacao = 0 

# Looping para realização de várias operações:
while operacao != 4:
    # Menu com 4 operações:
    print("\n","*"*15, "MENU DE OPERAÇÕES:", "*"*15,"\n")
    print("DIGITE [1]: Realizar Depósito\nDIGITE [2]: Realizar Saque\nDIGITE [3]: Consultar o ativo bancário (Saldo de todos os clientes somados)\nDIGITE [4]: Finalizar Programa\n")

    # Entrada da operação escolhida pelo usuário:
    operacao = int(input("Digite a operação que deseja realizar: "))

    # 1° OPERAÇÃO:
    if operacao == 1:
        codigo_deposito = int(input("Código da conta para o depósito: "))
        # Verificando se o código digitado existe na lista:
        
        if codigo_deposito in codigos_lista:
            # Utilizando o enumerate() para capturar as posições e os valores da lista:
            for indice, valor in enumerate(codigos_lista): 
                
                # Estrutura que verifica se é possível depositar esse valor:
                while codigo_deposito == valor: 
                    saldo_adicional = float(input("Digite o valor que deseja depositar: "))
                    
                    # Mensagem de erro
                    if saldo_adicional < 0:
                        print("\nValor para depósito totalmente inválido!")
                        break

                    # Exibindo: 
                    else:
                        # Adicionando valor na mesma posição referente ao código da conta
                        print("\nDEPOSITANDO...")
                        sleep(2) # 2s de espera
                        saldos_lista[indice]+=saldo_adicional 
                        print(f"\nConta: {codigo_deposito}")
                        print(f"Saldo atualizado para: R${saldos_lista[indice] :.2f}")
                        break
        
        # Código não cadastrado
        else:
            print("\n","="*10,"CÓDIGO DE CONTA NÃO CADASTRADO!","="*10)
            continue

    # 2° OPERAÇÃO:
    elif operacao == 2:
        codigo_saque = int(input("Código da conta para o saque: "))
         # Verificando se o código digitado existe na lista:
        if codigo_saque in codigos_lista:
            # Utilizando o enumerate() para capturar as posições e os valores da lista:
            for indice, valor in enumerate(codigos_lista):
        
                # Estrutura que verifica se o valor é possível de ser sacado:
                while codigo_saque == valor:
                    saldo_saque = float(input("Digite o valor que deseja sacar: "))    
                    
                    # Mensagem de erro: 
                    if saldo_saque > saldos_lista[indice]:
                        print(f"\nSaldo insuficiente!")
                        break
                    
                    # Mensagem de erro:
                    elif saldo_saque < 0:
                        print("\nValor totalmente inválido!")
                        break

                    # Exibindo:
                    else:
                        # Atual:
                        print("\nSACANDO...")
                        sleep(2) # 2s de espera
                        print(f"\nValor do saque: {saldo_saque :.2f}")
                         # Adicionando valor na mesma posição referente ao código da conta
                        saldos_lista[indice]-=saldo_saque
                        # Saldo atualizado:
                        print(f"Saldo atualizado para: {saldos_lista[indice] :.2f}")
                        break

        # Código não cadastrado
        else: 
            print("\n","="*10,"CÓDIGO DE CONTA NÃO CADASTRADO!","="*10)
            continue

    # 3° OPERAÇÃO:
    elif operacao == 3:
        print("\nCONSULTANDO O ATIVO BANCÁRIO...")
        sleep(2) # 2s de espera
        # Exibindo:
        ativo_bancario = sum(saldos_lista) # Função que soma todos os valores da lista
        print(f"ATIVO BANCÁRIO: R${ativo_bancario :.2f}")

    # 4° OPERAÇÃO:
    elif operacao == 4: 
        # Finalizando...
        print("\nFinalizando o programa...")
        sleep(2) # 2s de espera
        print("Programa finalizado!\n")
    
    # Mensagem de erro:
    else:
        print("\nERRO: OPERAÇÃO INEXISTENTE (OBSERVE O MENU)!")
        continue

# Fim!