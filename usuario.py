class Usuario:
    #nombre_del_banco = "Banco del Sol"
    def __init__(self,balance=0 ):
        self.balance = balance
    
        
    

    def hacer_retiro(self,monto):
        if (self.balance- monto < 0):
            print("Saldo insuficiente")
        else:
            self.balance = self.balance - monto
    
    def hacer_deposito(self,monto):
        self.balance = self.balance + monto
    
    def mostrar_balance(self):
        print(f'"su saldo es:"{self.balance}')

    def transferir_dinero(self,otro_usuario,monto):
        otro_usuario.hacer_deposito(monto)
        self.hacer_retiro(monto)
        print("operacion transferencia realizada")

        
usuario1=Usuario()
usuario1.hacer_deposito(100)
usuario1.hacer_deposito(200)
usuario1.hacer_deposito(200)
usuario1.hacer_retiro(200)
usuario1.mostrar_balance()

usuario2=Usuario()
usuario2.hacer_deposito(100)
usuario2.hacer_deposito(800)
usuario2.hacer_retiro(100)
usuario2.hacer_retiro(200)
usuario2.mostrar_balance()
usuario2.transferir_dinero(usuario1,200)
usuario2.mostrar_balance()

usuario3=Usuario()
usuario3.hacer_deposito(1000)
usuario3.hacer_retiro(100)
usuario3.hacer_retiro(100)
usuario3.hacer_retiro(100)
usuario3.mostrar_balance()