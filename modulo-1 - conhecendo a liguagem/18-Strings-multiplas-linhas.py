# São definidas informando 3 aspas simples ou duplas durante a atribuição.
# Elas podem ocupar varias linhas de código, e todos os espaços em branco são
#incluidos no final da string

nome = "Felipe"
# utlizando a strings de multiplas linhas
mensagem = f"""
olá meu nome é {nome},
Eu estou aprendendo Pyhton.
"""
# Nesse metodo a mensagem permanece os recuos
msg = f'''
    olá meu nome é {nome},
    Eu estou aprendendo Python.
        Esta mensagem tem diferentes recuos.
'''
print(mensagem)
print(msg)