#conhecendo métodos uteis da classe string
curso = "pYthon"
print("Aula 15--Strings--")
print(curso)
#converte tudo para maiusculo
print("Converte tudo para maiusculo")
print(curso.upper())
#converte tudo para minusculo
print("Converte tudo para minusculo")
print(curso.lower())
#converte a primeira letra para maiusculo
print("Converte a primeira letra para maiusculo")
print(curso.title())

print("-------------------------")
print("Eliminando os espaços")

curso = " Python "
print(curso)

#eliminando os espaços 
print("Eliminando os espaços")
print(curso.strip())
#eliminando os espaços a direita
print("Eliminando os espaços a direita")
print(curso.rstrip())
#eliminando os espaços a esquerda
print("Eliminando os espaços a esquerda")
print(curso.lstrip())
print("-------------------------")
print("Junções e centralização")
curso = "Python"
print(curso)
#centralizando a string
print("centralizando a string")
print(curso.center(10))
#fazendo junções de caracteres
print("fazendo junções de caracteres")
print(".".join(curso))

