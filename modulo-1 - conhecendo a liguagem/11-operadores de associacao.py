#Este operador é case sensitive
curso = "Cruso de Python"
frutas = ["laranja","uva","limao"]
saques = [1500,100]

#usando o operador de associação
teste = "Python" in curso
print(teste)

#usando o operador de associação em negação
teste1 = "maça" not in frutas
print(teste1)

#exemplo de falso
dinheiro = 200 in saques
print(dinheiro)