#Utilizando loop infinito com continue e break

print("tilizando loop infinito com continue e break")
print("--------------------------------------------")

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        #para a execução
        break

    if numero % 2 == 0:
        #pula a execução
        continue

    print(numero)