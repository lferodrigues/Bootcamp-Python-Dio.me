#lendo valores com a funçao input
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")
#imprimindo valores na tela
print(nome,idade)
#\n que da a quebra de linha
print(nome,idade, end="...\n")
#sep é usado para demarcar o seprador
print(nome,idade, sep="#")
#utilizando o sep + end
print(nome,idade,sep=" # ", end="...\n")
