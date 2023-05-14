#Aprender como o interpretador python utiliza a identação do código para delimitar os blocos de comando.

saldo = 800
vlr=0
#Inicio do bloco do método
def sacar(valor):
    #inicio do bloco do if
    if saldo >= valor:
        print(valor,"sacado!")
    #fim do bloco do if
#fim do bloco do metodo.


#chamando a função
sacar(100)


def depositar(valor):
    saldo = 500
    saldo+=valor
    print("o valor depositado foi de:",valor)
    print("Seu saldo em conta é: ",saldo)

depositar(200)