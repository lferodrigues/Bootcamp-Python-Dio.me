'''
Iterar listas
A forma mais comum para percorrer os dados de uma lista é utilizando o comando for
'''
carros = ['gol','celta','azera']

for carro in carros:
    print(carro)

print("")
print("Função Enumerate")

'''
Função enumerate

As vezes é necessário saber qual o indice do objeto dentro do laço for.
Para isso utilizamos a função enumerate
'''
for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")

print("Compreensão de listas")
'''
A compreensão de lista oferece uma sintaxe mais curta quando voce deseja:
criar uma nova lista com base nos valores de uma lista existente (filtro) ou
gerar uma nova lista aplicando alguma modificção nos elementos de uma lista existente.

'''
#Senario de filtro
numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        #append é uma forma de adcionar valores da lista

print(pares)
print("Usando o comprend rand")
numeros=[3,13,22,44,55,66,99,666]
pares = [numero for numero in numeros if numero % 2 == 0]
#primeiro se passa o retorno, aonde sera buscado a informação, depois se passa a iteração (o for) e a terceira e o filtro (if)
print(pares)

