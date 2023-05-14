#Sao operadores utilizados para comparar se dois ou mais objetos testados ocupam a mesma posição 
#na memoria

curso = "Curso de pyton"
nome_curso= curso
saldo,limite=200,200

compara_curso = curso is nome_curso
print(compara_curso)

#identifica com negaçao,mostra se nao estao usando a mesma regiao de memoria
compara_curso1=curso is not nome_curso
print(compara_curso1)

testa_saldo=saldo is limite
print(testa_saldo)
