#O fatiamento de strings é uma tecnica utilizada para retornar subtrings
#(partes da string original), informando inicio (strat),fim(stop) e passo(step):[start:stop[,step]].
nome = "Felipe Rodrigues"
#para acessar a string passamos entre colchetes o indice, sempre começando em 0

print(nome[0])

#imprime ate o 9º caracter
print(nome[:9])
#imprime um intervalo
print(nome[3:10])
#imprime um conjunto de caracteres ate uma final nao definido pelo o usuario
print(nome[2:])
#imprime tudo
print(nome[:]) 
#imprime ao contrario
print(nome[::-1]) 
#imprimindo a informação apartir do intervalo e do step
print(nome[3:10:2])