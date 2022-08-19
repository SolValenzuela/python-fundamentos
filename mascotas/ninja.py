# implementar __init__( nombre, apellido, premios, comida_mascota, mascota )
class Ninja:
    def __init__(self, nombre, apellido, premio, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premio = premio
        self.comida_mascota = comida_mascota
        self.mascota = mascota

# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        print(f'{self.nombre} la saca a caminar')
        self.mascota.jugar()
        return(self)

# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()    
    def alimentar(self):
        print(f'{self.nombre} la alimenta')
        self.mascota.comer()
        return(self)

# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()    
    def banar(self):
        print(f'{self.nombre} la bana')
        self.mascota.sonido()
        return(self)
    
    def __repr__(self):
        return (f'{self.nombre} tiene una mascota  {self.mascota}')
        