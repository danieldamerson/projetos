menu= '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''
saldo=0
limite=500
extrato=" "
numero_saques=0
LIMITE_SAQUES=3


while True:
    opcao=input(menu)
    if opcao =="d":
        valor = float(input("informe o valor"))


        if valor >= 1:
            saldo += valor  
            extrato += f"Depósito: R$ {valor:.2f}\n"


        else:
            print("digite um valor válido")


    elif opcao=="s":
        valor = float(input("informe o valor que vc quer sacar: "))
        excedeu_saldo =  valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O limite máximo é de 500")

        elif excedeu_saques:
            print("Operação falhou! Você só pode fazer 3 saques por dia")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1


    elif opcao=="e":
        print("\n##############EXTRATO#############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#################################################")



    elif opcao=="q":
        break


    else:
        print("Operação inválida, por favor selecione uma válida")
        