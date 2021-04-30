class Conta:
    titular = ""
    numero = 0
    saldo = 0
    
    def _init_(self,titular,numero):
        self.titular = titular
        self.numero = numero
        
    def depositar(self,valor):
        self.saldo += valor
        print("Valor de "+str(valor)+" foi depositado na conta "+str(self.numero)+" de "+str(self.titular))
        
    def sacar(self,valor):
        if(self.saldo - valor >= 0):
            self.saldo -= valor
            print("Valor de "+str(valor)+" foi sacado na conta "+str(self.numero)+" de "+str(self.titular))
        else:
            print("Saldo insuficiente")
            

class ContaCorrente(Conta):
    limite = 100
    
    def anuidade(self):
        self.saldo -= 50
        
    def sacar(self,valor):
        if(self.saldo + self.limite - valor >= 0):
            self.saldo -= valor
            print("Valor de "+str(valor)+" foi sacado na conta "+str(self.numero)+" de "+str(self.titular))
        else:
            print("Saldo insuficiente")
    

class Banco:
    nome = ""
    contas = []
    
    def _init_(self, nome):
        self.nome = nome
        
    def buscar(self,numero):
        for i in self.contas:
            if i.numero == numero:
                return i
            

c1 = ContaCorrente()
c2 = Conta()

c1.sacar(120)
c2.sacar(50)

print(c1.saldo)
print(c2.saldo)

bb = Banco()

bb.contas.append(c1)
bb.contas.append(c2)


if(bb.buscar(123) != None):
    print(bb.buscar(1234).saldo)
else:
    print("Nao existe")