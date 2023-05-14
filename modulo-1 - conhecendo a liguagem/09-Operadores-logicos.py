#opedores logicos e de comparação
saldo = 1000
saque = 200
limite = 100

#retorna um valor booleano
print("Saldo >= saque")
print(saldo >= saque)

#Usando o operador E
print("saldo >= saque and saque <= limite")
print(saldo >= saque and saque <= limite)

#Usando o operador ou
print("saldo >= saque or saque <= limite")
print(saldo >= saque or saque <= limite)

#operador de negação
#Lista em python
contatos_emergencia = []

print("not 1000 > 1500")
print(not 1000 > 1500)

print("not contatos_emergencia")
print(not contatos_emergencia)

print("not saque 1500")
print(not "saque 1500;")

print("not")
print(not "")

#Parenteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

print("saldo >= saque and saque <= limite or conta_especial and saldo >= saque")
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

print("(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)")
exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)