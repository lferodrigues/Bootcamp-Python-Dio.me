print("Metodo .sort[]")
#Metodo .Sort[] é utilizado para ordenar uma lista.
linguagens = ["python","JS","C","Java","csharp"]
linguagens.sort()
print(linguagens)
#mostrando a ordem reversa
linguagens.sort(reverse=True)
print(linguagens)
#mostrando de arcordo com o tamanho da string
linguagens.sort(key=lambda x: len(x))
print(linguagens)
#mostrando de arcodo com o tamanho da sring, porem em ordem reversa
linguagens.sort(key=lambda x: len(x),reverse=True)
print(linguagens)
print('')

print("Metodo len[]")
#Metodo .Len[] mostra o tamanho da string
tamanho = len(linguagens)
print(tamanho)
print('')

print("Metodo sorted")
#O metodo sorted, é uma funçao bet-win ou seja, ja e uma funçao embarcada no sistema
#E essa funçaõ tambem serve para ordenar 
linguagens = ["python","JS","C","Java","csharp"]

print(sorted(linguagens,key=lambda x: len(x)))

print(sorted(linguagens,key=lambda x: len(x),reverse=True))