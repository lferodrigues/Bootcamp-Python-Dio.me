# [].count é utilizado para contar quantas vezes um objeto aparece dentro da sua lista
cores = ["vermelho","azul","verde","azul"]
print("Metodo count[]")
print(cores.count("vermelho"))
print(cores.count("azul"))

print("Metodo extends[]")
#[].extends é utlizado para fundir dados de uma lista com outra
linguagens = ["python","js","c"]

print(linguagens)
linguagens.extend(["java","php"])
print(linguagens)

print("Metodo index[]")
#[].index é utilizado para encontrar a primeira posição de um objeto dentro da lista
linguagens = ["python","js","c","java"]

poisicao = linguagens.index("java")
print("o objeto java encontra-se na poição de numero: ",poisicao)
poisicao = linguagens.index("c")
print("o objeto c encontra-se na poição de numero: ",poisicao)

print("Metodo pop[]")
#[].pop é utilizado para remover um objeto da lista
linguagens = ["python","js","c","java"]
print(linguagens)

#removendo o ultimo objeto da lista
linguagens.pop() 
print(linguagens)
#removendo o segundo objeto da lista
linguagens.pop(1)
print(linguagens)

print("Ultilizando o metodo .remove[]")
#remove[] e um segundo metodo para excluir um objeto de dentro da lista
#Diferente do pop, ao enves de passar a posição, voce passa o elemento em si

linguagens = ["python","js","c","java"]
print(linguagens)
linguagens.remove("js")
print(linguagens)

print("Metodo reverse[]")
#[].reverse é utilizado para inverter a ordem dos elementos da lista
linguagens = ["python","js","c","java"]
print(linguagens)
linguagens.reverse()
print(linguagens)

