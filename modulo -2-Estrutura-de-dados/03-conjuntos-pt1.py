#Entendo o funcionamento da estrutura de dados set
'''
Um set é uma coleção que não possui objetos repetidos,
que usamos sets para represntar conjuntos matematicos ou 
eliminar itens duplicados de um iterável.
'''
print("Exemplos utilizando metodo set")

#O set não garante a ordem

#removendo valores duplicados de uma lista
numeros = set([1,2,3,1,3,4])
print(numeros)

#como o set espera um iteravel no seu construtor, nos podemos passar uma string

#removendo caracteres duplicados na string
letras = set("abacaxi")
print(letras)

#removendo palvaras duplicadas dentro de uma tupla
carros = set(("palio","gol","celta","palio"))
print(carros)

#removendo palavras duplicadas dentro de uma chave
linguagens = {"python","java","python"}
print(linguagens)

print("")
print("Acessando os dados")
'''
Conjuntos em Python não suportam indexação e nem fatiamento,
caso queira acessar os seus valores é necessario
converter o conjunto para lista.
'''
print("Exemplo")

numeros = {1,2,3,2}
#convertendo conjunto em lista
numeros = list(numeros)

print(numeros[0])