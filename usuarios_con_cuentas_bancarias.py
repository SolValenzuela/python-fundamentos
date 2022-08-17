from cuenta_bancaria import CuentaBancaria

class Usuario:
    
    def __init__(self,name):
        self.name= name
        self.balance=balance= 0
        self.cuenta=CuentaBancaria()

    #def hacer_retiro(self,monto): (metodo anterior)
    #    if (self.balance- monto < 0):
    #        print("Saldo insuficiente")
    #    else:
    #        self.balance = self.balance - monto
    #    return(self)    

    def retiro(self,monto):     #metodo actualizado
        self.cuenta.retiro(monto)
        return(self)
    
    #def hacer_deposito(self,monto):    (metodo anterior)
    #    self.balance = self.balance + monto
    #    return(self)
    
    def deposito(self,monto):     #metodo actualizado
        self.cuenta.deposito(monto)
        return(self)

    #def mostrar_balance(self):    (metodo anterior)
    #    print(f'{self.name} su saldo es: {self.balance}')
    #    return(self)

    def mostrar_info_cuenta(self):
        self.cuenta.mostrar_info_cuenta()
        return(self)

    #def transferir_dinero(self, otro_usuario, monto):
    #    otro_usuario.hacer_deposito(monto)
    #    self.hacer_retiro(monto)
    #    print(f'{self.name} ha realizado una transferencia  ')
    #    return(self)

sol=Usuario("Sol")
carlota=Usuario("Carlota")
pepito= Usuario("Pepito")

sol.deposito(1000).retiro(100).mostrar_info_cuenta()

carlota.deposito(8000).retiro(900).mostrar_info_cuenta()

pepito.deposito(8999).retiro(799).mostrar_info_cuenta()

