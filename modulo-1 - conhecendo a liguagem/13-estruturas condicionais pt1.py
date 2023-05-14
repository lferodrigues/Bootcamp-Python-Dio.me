#Etapa 1 If/else/elif 
print("1 - Trabalhando com If/else/elif")
print("--------------------------------")
saldo=2000.0
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Estrato: "))
saque=0.0
if opcao == 1:
    valor = float(input("Informe o valor a ser sacado: "))
    
    if valor<=saldo:
        saque=saldo-valor
        saldo=saque
        print("Saque realizado com sucesso! seu novo saldo em conta é: ",saldo)
    else:
        print("Saldo insuficiente")

elif opcao==2:
    print("Exibindo o extrato...")

else:
    print("Opção Invalida!")
