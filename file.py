num1 = 42       #variable declaration/Data Types Primitive:Numbers
num2 = 2.3      #variable declaration/Data Types Primitive:Numbers
boolean = True      #variable declaration/Data Types Primitive:Boolean
string = 'Hello World'       #variable declaration/Data Types Primitive:Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #Data Types,Composite:List,initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana')   #tuples
print(type(fruit))  #funcion comun
print(pizza_toppings[1]) #Data Types,Composite:List=>access value
pizza_toppings.append('Mushrooms')  #metodo para manipular lista/agrega elemento 
print(person['name'])   #list/access value
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2]) #imprime 2°elemento de tuples

if num1 > 45:       #conditional =>if
    print("It's greater")
else:   #conditional else
    print("It's lower")

if len(string) < 5:     #conditional if =>length check
    print("It's a short word!")
elif len(string) > 15:     #conditional =>elif
    print("It's a long word!")
else:      #conditional =>if
    print("Just right!")

for x in range(5):  #for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):   #while loop/start
    print(x)
    x += 1 #while loop/increment

pizza_toppings.pop()    #List:delete value
pizza_toppings.pop(1)   #List:delete value

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:  #for loop
    if topping == 'Pepperoni':  #conditional
        continue
    print('After 1st if statement')
    if topping == 'Olives':     #conditional
        break   #for loop=>break

def print_hello_ten_times():    #function
    for num in range(10):
        print('Hello')  

print_hello_ten_times()

def print_hello_x_times(x): #function
    for num in range(x):
        print('Hello') #return

print_hello_x_times(4) #function/parameter

def print_hello_x_or_ten_times(x = 10): #function/parameter
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()    #function/parameter
print_hello_x_or_ten_times(4)   #function/parameter


"""
Bonus section       #comment multiline
"""

# print(num3)   #comment single line/NameError: name <variable name> is not defined
# num3 = 72     #comment single line
# fruit[0] = 'cranberry'    #comment single line/TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])    #comment single line/KeyError: 'favorite_team'
# print(pizza_toppings[7])      #comment single line/IndexError: list index out of range
#   print(boolean) #comment single line     #comment single line/IndentationError: unexpected indent
# fruit.append('raspberry')     #comment single line/AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)      #comment single line/AttributeError: 'tuple' object has no attribute 'pop'