#basicamente e passar o construtor e a variavel que voce quer converter

print('convertendo de inteiro para float')
print('')
preco=10
print(preco)

preco=float(preco)
print(preco)

preco = 10/2
print(preco)

print('----------------')

print('convertendo float para int')
print('')
preco=10.30
print(preco)

preco = int(preco)
print(preco)

print('-----------')

print('conversão por divisão')
preco=10
print(preco)

print(preco / 2)
#divisao com duas // em um numero interio ele preserva o numero inteiro.
print(preco //2)
print('--------------')

print("convertendo numero para string")
print("")

preco = 10.50
idade = 28

print(str(preco))

print(str(idade))
#Usar variaveis para converter
#passa o "f" de formatação e concatena com {}
texto = f"idade {idade} preco {preco}"
print(texto)

print("-----------")

print("String para numero")

preco = "10.50"
idade = "28"

float(preco)
print(preco)
int(idade)
print(idade)