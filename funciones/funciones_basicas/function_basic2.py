#cuenta regresiva

l=[]
for i in range(0,20):
    l.append(i)
l.reverse()
print(l)

#otra forma de cuenta regresiva
def number(lim):
    x=[]
    for i in range(0,lim):
        x.append(i)
    return x

x=number(10)
x.reverse()
print(x)


#imprimir y devolver.Ej:imprimir_y_devolver([1,2])debe imprimir 1 y devolver2
def imprime_y_devuelve(x):
    print(x[0])
    return x[1]
l=imprime_y_devuelve([5,7])
#print(l)

#Primero más longitud: crea una función que acepte una lista 
# y devuelva la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)

def devuelvesuma_y_longitud(a):
    b=a[0]+a[1]
    print(b)
    print(len(a))

devuelvesuma_y_longitud([3,4,5,6,7])

#Valores mayores que el segundo: 
# escribe una función que acepte una lista 
# y cree una nueva que contenga solo los valores de la lista original 
# que sean mayores que su segundo valor. 
# Imprime cuántos valores son y luego devuelve la lista nueva. 
# Si la lista tiene menos de 2 elementos, has que la función devuelva False
#Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def imprime_valores_mayores(c):
    # la lista tiene mas de 2 valores
    if len(c)<=2:
        return False
    # lista nueva 
    nueva_lista=[]
    for e in c:
        if e > c[1]:
            nueva_lista.append(e)
    # largo lista nueva
    largo=len(nueva_lista)
    print("numero de valores en lista nueva",largo)
    return (nueva_lista)

print(imprime_valores_mayores([5,2,3,2,1,4]))
print(imprime_valores_mayores([3]))


#Esta longitud, ese valor:
# escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, 
# y cuyos valores sean todos el valor dado.
#Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]


def largo_y_valor(f,g):
    l=[]
    for a in range(f):
        l.append(g)
    print(l)
    

largo_y_valor(4,5)


