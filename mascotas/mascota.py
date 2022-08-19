# implementa __init__( name , tipo , golosinas ):
class Mascota:
    def __init__(self,name,tipo,golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 0
        self.energia = 0

# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
    def dormir (self):
        print(f'{self.name} esta durmiendo')
        self.energia= self.energia + 25
        return(self)

# comer() - incrementa la energía de la mascota en 5 y la salud en 10   
    def comer (self):
        print(f'{self.name} esta comiendo')
        self.energia = self.energia + 5
        self.salud = self.salud + 10
        return(self)

# jugar() - incrementa la salud de la mascota en 5
    def jugar (self):
        print(f'{self.name} esta jugando')
        self.salud= self.salud + 5
        return(self)

# ruido() - imprime el sonido que produce la mascota
    def sonido (self):
        print(f'{self.name} dice grrrr')
        #return(self)
    
    def __repr__(self):
        return (f'\n********************************\n{self.name} es su {self.tipo}, su golosina favorita es {self.golosinas},\nsu nivel de salud es {self.salud} y su energia está en  {self.energia} \n *****************')