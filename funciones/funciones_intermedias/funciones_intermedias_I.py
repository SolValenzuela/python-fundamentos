#I Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1 Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

#2 Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name']="Bryant"
print(estudiantes)

#3 En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['futbol']="Andres"
print(directorio_deportes)

#4 Cambia el valor 20 en z a 30.
z[0]['y']=30
print(z)


#II Iterar a través de una lista de diccionarios

#Crea una función iterateDictionary(some_list)para que, 
# dada una lista de diccionarios, la función recorra cada diccionarios de la lista 
# e imprima cada llave y el valor asociado. 

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def itirateDictionary(lista):
    for estudiante in estudiantes:
        for x in estudiante:
            print(f'{x}- {estudiante[x]}',end=' , ')
        print('')
            

itirateDictionary(estudiantes)

#iterateDictionary(estudiantes) 
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel

#III Obtener valores de una lista de diccionarios

# Crea una función iterateDictionary2(key_name, some_list)que,
#  dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario.

def iterateDictionary2(key_name,some_list):
        for a in some_list:
            print(a[key_name])

iterateDictionary2('first_name',estudiantes)

iterateDictionary2('last_name',estudiantes)

# IV Iterar a través de un diccionarios con valores de lista
#Crea una función printInfo(some_dict)que, 
# dado un diccionario cuyos valores son todos listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista
# , y luego imprima los valores asociados 
# dentro de la lista de cada clave. Por ejemplo:

lista_de_compras={
    'frutas':['manzanas','platanos','peras','frambuesas'],
    'verduras':['papas','zapallo','cebollas','zanahorias','apio']
}

def printInfo(some_dict):
    for a in some_dict:        
        print(len(some_dict[a]),end=" ")
        print (a.upper())
        for b in some_dict[a]:
            print (b)
printInfo(lista_de_compras)







