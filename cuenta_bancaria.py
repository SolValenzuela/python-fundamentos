class CuentaBancaria:
    def __init__(self,tasa_de_interes=0.01, balance=0):
        self.tasa_de_interes=tasa_de_interes
        self.balance=balance

    #clase de usuario
    def deposito(self,monto):
        self.balance= self.balance + monto
        return(self)
        
        
    def retiro(self,monto):
        if (self.balance - monto <=5):
            print(f'Fondos insuficientes:cobrando tarifa $5')            
            self.balance=self.balance - monto -5
        else:
            self.balance=self.balance - monto
        return(self)


    def mostrar_info_cuenta(self):
        #print(200)
        print(f'tu saldo es {self.balance} con interes de {self.tasa_de_interes}')
        return(self)

    def generar_interes(self):
        print("interes generado:")
        interes_ganado=self.balance * self.tasa_de_interes
        print(f'intereses generados {interes_ganado}')
        self.balance= self.balance + interes_ganado
        return(self)
        

cuenta1= CuentaBancaria()
cuenta2= CuentaBancaria()
cuenta1.deposito(200).deposito(200).deposito(800).retiro(200)
cuenta1.mostrar_info_cuenta()

cuenta2.deposito(3000).retiro(1000).retiro(1050).retiro(950)
cuenta2.mostrar_info_cuenta()