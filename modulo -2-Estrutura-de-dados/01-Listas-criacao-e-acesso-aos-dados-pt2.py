'''
Listas podem armazenar todos os tipos de objetos Python,
portanto podemos ter listas que armazenam outras listas.
Com isso podemos criar estruturas bidmensionais (tabelas),
e acessar informando os índices de linha e coluna.
'''
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print("Imprimindo a matriz")
print(matriz[0])
#passando indice e coluna
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

'''
Fatiamento

Alem de acessar elementos diretamente, podemos extrair um conjunto
de valores de uma sequencia.
Para isso basta passar o índice inicial e/ou final para acessar o conjunto.
Podemos ainda informar quantas posições o cursor deve 'pular' no acesso

'''
lista = ["p","y","t","h","o","n"]

print(lista[2:])
print(lista[:3])
print(lista[::2])
print(lista[::-1])
print(lista[::])