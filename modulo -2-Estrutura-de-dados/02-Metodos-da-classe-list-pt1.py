#metodos da classe list

#1º metodo [].append

lista = []

lista.append(1)
lista.append("python")
lista.append([40,30,20])

print(lista)

#2º metodo [].clear

'''
Ele é utilizado quando quero limpar a minha lista
'''
lista.clear()
print(lista)

#3º metodo [].copy

'''
A lista, ela é um objeto mutavel, ou seja, se eu tenho um funçao dentro da lista e passo ela 
para dentro do codigo, ela sera alterada, para evitar isso usamos o cpy para copiar as informações 
para uma nova lista
'''

lista = [1,"Python",[40,30,20]]

l2 = lista.copy()

print(lista)

print(id(l2),  id(lista))