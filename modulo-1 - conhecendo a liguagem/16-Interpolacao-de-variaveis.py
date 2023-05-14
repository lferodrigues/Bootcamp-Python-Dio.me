#Interpolação de variaveis
# Exitem 3 formas de intorpar
# A primeira é usando o  sinal %
# A segunsa é usando o metodo format e a terceira é utilizando o metodo f strings
# A terceira não é muito utilizada no python3

print("Ultilizando a %")
print("----------------")

nome = "Felipe"
idade = 25
profissão = "Programdador"
linguagem = "Python"

#Voce vai usar %s quando quer colocar valores do tiṕo string
#Voce vai usar %d quando quer colocar valores do tiṕo inteiros
#Voce vai usar %f quando quer colocar valores do tiṕo Float

print("Olá me chamo %s.Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s."
      % (nome, idade, profissão, linguagem))

print("--------------------------------------------------------------------------------------------")
print("Utilizando o metodo format")

#E passado por numeração de variavel dentro das chaves para demarcar aonde vai cada informção
print("Olá me chamo {3}.Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}."
      .format(linguagem,profissão,idade,nome))
print("--------------------------------------------------------------------------------------------")
print("Utilizando o metodo format e retornando informação por nome")
print("Olá me chamo {nome}.Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculado no curso de {linguagem}."
      .format(nome=nome,idade=idade,profissão=profissão,linguagem=linguagem))
print("--------------------------------------------------------------------------------------------")
print("Utilizando o metodo f strings")
print (f"olá,me chamo {nome}.Eu tenho {idade} anos de idade, trabalho como {profissão} e estou matriculo no curso de {linguagem}.")
print("--------------------------------------------------------------------------------------------")
print("Formatar strings com f-strings")
PI = 3.14159
print(f"valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}")



