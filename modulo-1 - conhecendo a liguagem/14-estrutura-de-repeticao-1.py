# Utilizando o comando for
print("Utilizando o comando for")
print("------------------------")

texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        #o comando upper transforma a letra em maiuscula
        print(letra, end="")

else:
    print() #adciona linha quebrada
