#Metodos da classe set
print("{}.unio")
#Esse metodo junta dois conjuntos

conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

print("")
print("{}.intersection")
# Esse metodo mostra a intercessao dos conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_c = conjunto_a.intersection(conjunto_b)

print(conjunto_c)

print("")
print("{}.difference")
# Esse metodo mostra a diferença dos conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_c = conjunto_a.difference(conjunto_b)
print(conjunto_c)
conjunto_c = conjunto_b.difference(conjunto_a)
print(conjunto_c)

print("")
print("{}.symmetric_difference")
#Esse metodo retorna todos os elementos que nao estao na intercessao
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_c = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_c)

print("")
print("{}.issubset")
#Essa função verifica se um conjunto esta contido em outro

conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_c = conjunto_a.issubset(conjunto_b)
print(conjunto_c)
conjunto_c = conjunto_b.issubset(conjunto_a)
print(conjunto_c)

print("")
print("{}.issuperset")
#Verifica se o conjunto A é superset do B ou vice-versa'
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}

conjunto_c = conjunto_a.issuperset(conjunto_b)
print(conjunto_c)
conjunto_c = conjunto_b.issuperset(conjunto_a)
print(conjunto_c)

print("")
print("{}.isdisjoint")
#Retornar True caso não haja elementos comuns entre os conjuntos
conjunto_a = {1, 2, 3,4, 5}
conjunto_b = {7,8 ,9}
conjunto_c = {1,0}

conjunto_d = conjunto_a.isdisjoint(conjunto_b)
print(conjunto_d)
conjunto_d = conjunto_a.isdisjoint(conjunto_a)
print(conjunto_d)

print("")
print("{}.add")
#Adicionando elemento ao conjunto

sorteio = {1,23}

sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(26)
print(sorteio)
#Se passar um elemento que ja existe, o mesmo é ignorado.
sorteio.add(25)
print(sorteio)

print("")
print("{}.clear")
#Limpa todos os itens de uma lista
sorteio = {1,23}
sorteio.clear() 
print(sorteio)