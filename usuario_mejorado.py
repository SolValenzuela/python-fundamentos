class Usuario:
    
    def __init__(self,name):
        self.name= name
        self.balance=balance= 0

    def hacer_retiro(self,monto):
        if (self.balance- monto < 0):
            print("Saldo insuficiente")
        else:
            self.balance = self.balance - monto
        return(self)    
    
    def hacer_deposito(self,monto):
        self.balance = self.balance + monto
        return(self)
    
    def mostrar_balance(self):
        print(f'{self.name} su saldo es: {self.balance}')
        return(self)

    def transferir_dinero(self, otro_usuario, monto):
        otro_usuario.hacer_deposito(monto)
        self.hacer_retiro(monto)
        print(f'{self.name} ha realizado una transferencia  ')
        return(self)

        
sol=Usuario("Sol")
sol.hacer_deposito(100)
sol.hacer_deposito(200)
sol.hacer_deposito(200)
sol.hacer_retiro(200)
sol.mostrar_balance()
sol.hacer_deposito(1000).hacer_retiro(200).mostrar_balance()

carlota=Usuario("Carlota")
carlota.hacer_deposito(100)
carlota.hacer_deposito(800)
carlota.hacer_retiro(100)
carlota.hacer_retiro(200)
carlota.mostrar_balance()
carlota.transferir_dinero(sol,200)
carlota.mostrar_balance()
sol.mostrar_balance()

pepito= Usuario("Pepito")
pepito.hacer_deposito(1000)
pepito.hacer_retiro(100)
pepito.hacer_retiro(100)
pepito.hacer_retiro(100)
pepito.transferir_dinero(carlota,200)
pepito.mostrar_balance()
