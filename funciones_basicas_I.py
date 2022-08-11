#1
def número_de_grupos_alimentarios():
    return 5
print(número_de_grupos_alimentarios())  #imprime 5

#2
def número_de_ramas_militares():
    return  5
print(número_de_dias_en_una_semana_de_silicona_o_lados_del_triangulo()+número_de_ramas_militares())
# la variable número_de_dias_en_una_semana_de_silicona_o_lados_del_triangulo no está definida, por lo tanto, Error

#3
def número_de_libros_en_espera():
    return  5
    return  10
print(número_de_libros_en_espera())
#imprime 5 porque la funcion fue invocada una vez y devuelve el primer "return"

#4
def número_de_dedos():
    return  5
print(10)
print(número_de_dedos())
#imprime 5 ,pero no 10

#5
def número_de_lagos_grandes():
        print(5)
x = número_de_lagos_grandes()
print(x)
# imprime 5 ,pero x no tiene valor

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#imprime (b+c) cada vez que se le asigna parametros, es decir 3(por 1+2) y 5 (que corresponde a 2+3)

#7
def concatenar(b,c):
    return str(b)+str(c)
="función de soporte python from-rainbow">print(concatenar(2,5))
#devuelve error porque no hay variable antes del =

#8
def número_de_océanos_o_dedos_o_continentes():
    b = 100
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(número_de_oceános_o_dedos_o_continentes())
# no está definida la variable número_de_oceanos_o_dedos_o_continentes, devuelve error


#9
def número_de_días_en_una_semana_silicona_o_lados_del_triángulo(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3))
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))
print(número_de_días_en_una_semana_silicona_o_lados_de_triángulo(2,3) + número_de_días_en_una_semana_silicona_o_lados_de_triángulo(5,3))
#Error,no hay variable para almacenar los parametros dados porque no está definida.

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#devuelve 8

#11
b = 500
print(b)
def foobar():
    b ="operador de palabra clave from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)
#imprime 500 500 de la variable declarada fuera de la funcion/ foobar() no arroja resultado porque b en la funcion compara string con numero,dará error

#12
b= 500
print(b) #imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b) # imprime 500
foobar() # imprime 300
print(b) #imprime 500


#13
b = 500
print(b) #imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b) #imprime 500
b=foobar() #imprime 300
print(b) #imprime 300


#14
def foo():
    print(1) #imprime 1
    bar()
    print(2) #imprime 2
def bar():
    print(3) #imprime 3
foo()
#se imprime lo que está dentro de la funcion porque fue invocada,pero no retorna ningun valor para almacenar

#15
def foo():
    print(1) #imprime 1
    x = bar()
    print(x) #imprime 5
    return 10
def bar():
    print(3) #imprime 3
    return 5
y = foo() 
print(y)#imprime 10
#se va imprimiendo en el siguiente orden= 1,3,5,10


































