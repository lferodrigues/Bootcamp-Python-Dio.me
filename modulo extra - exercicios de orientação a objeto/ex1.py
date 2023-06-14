
class Pessoa:

    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = 21

    def engordar(self):
        self.peso = 60.0   

    def emagrecer(self):
        self.peso = 40.00

    def crescer(self):
         if self.idade < 21:
            self.self.altura +=0.5

    def mostrapessoa(self):
        print("Nome: ", {self.nome})
        print("Idade: ",{self.idade})


pessoa1 = Pessoa("Felipe",25,72.0,1.75)

pessoa1.mostrapessoa()


