from mascota import Mascota
from ninja import Ninja

name=Mascota("Carlota","gata","galleta")
print(name)
name.dormir().jugar().dormir()
print(name)

ninja_rojo=Ninja("Ninja","rojo","cookie","peluche",name)
print(ninja_rojo)

ninja_rojo.caminar().alimentar().banar().alimentar()
print(ninja_rojo)













