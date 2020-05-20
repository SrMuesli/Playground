# Coments

def function1(): # Aqui se está definiendo la funcion "function1". ---- Son super importantes los dos puntos del final, sino no chusca.---
    print("Hi there")
    print("I'm using whatsapp")
print("Fuera de la funcion")
function1() # Con esto se llama a la funcion.

# Mapping
def function2(x): #La "X" es un "argument".
    return 2*x #Esto va a devolver la "X" por 2.

a = function2(3) # Aqui se asigna la variable "a" con el resultado de function2", pero en el lugar de la "X" pone un "3".

print(a)

b = function2(8) # Aqui se asigna la variable "b" con el resultado de "function2", pero multiplicado por "8".

print(b)

def function3(z, y): # Aqui hay mas de un "argument" en la misma funcion.
    return z + y # es la suma de "z + y".

e = function3(3, 7) # Así que aquí tengo que darle los valores necesarios a ese argumento.

print(e)

def function4(k):
    print(k) # Me va a mostrar el valor del "argument".
    print("Esta funcion va a multiplicar lo de arriba x3") # Va a mostrar este texto.
    return 3*k # Me va a mostrar el resultado de multiplicar por 3 el "argument".

o = function4(6)

print(o)

def function5(Some_argument):
    print(Some_argument)
    print("Weeeeee")

function5(4)