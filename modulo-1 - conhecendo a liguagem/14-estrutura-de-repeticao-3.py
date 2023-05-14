#Utilizando o comando while

print("Utilizando o comando while")
print("--------------------------")

opcao = -1

while opcao !=0:
    opcao = int(input("[1] Sacar \n[2] extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("...Sacando...")
    elif opcao == 2:
        print("...Exibindo o extrato...")
    if opcao > 9:
        print("...Opção invalida! saindo do sistema...")
        break
else:
    print("Obrigado po usar o nosso sistema bancario, até logo!")