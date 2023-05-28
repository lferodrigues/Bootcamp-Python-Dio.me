'''
Listas em pyhton podem armazenar de maneira sequencial qualquer tipo de objeto.
Podemos criar listas utilizando os construtor list, a funçãao range ou colocando
valores separados por vírgula dentro de colchetes.
Lista são objetos mutáveis, portanto podemos alterar valores após a criação.
Em Python tudo é objeto.
'''
#lista cheia
frutas = ["laranja","maca","uva"]
print(frutas)

#lista vazia
frutas =  []
print(frutas)

#usando o metodo list que retorna a separação de letra por letra e numero por numero
letras = list("python")
print(letras)

#usando o metodo list com numeros randometros
numeros = list(range(10))
print(numeros)

#usando lista e recebendo valores de diferentes tipos
carro = ["Ferrari","F8",420000,2020,2900,"São Paulo",True]
'''
A lista é uma sequencia, portanto podemos acessar seus dados utilizando indices.
Contamos o índice de determinada sequencia a partir do zero.
'''
print("Mostrando o valor, atraves da referencia")
print(carro[0])
print(carro[4])

#acessando os valores de modo negativo
'''
Passa o valor negtivo para pegar a informação contida na string de determinado valor  soq eu contado da direita para esquerda
ou seja inverso
'''
print(carro[-4])