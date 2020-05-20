# For Loooooooooooooooooops

# Ejercicio A

a = ["banana", "apple", "microsoft"]

for element in a: # Imprime cada "elemento" de la lista.
    print(element)



# Ejercicio B

b = [10, 20, 10]

total = 0 # Creo la variable "total" con el valor de 0.

for x in b: # En lugar de "element" se puede usar cualquier cosa. Entiendo que se comporta como si fuese una variable.
    total = total + x # Esto va a sumar los valores de "b" a la variable total, por lo que recibiremos la suma de todos esos valores.

print(total) # Imprime la variable "total".


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Range



# Ejercicio A

range(1, 5) # Crea un rango de valores desde 1 hasta 5 (no incluye 5).

c = list(range(1,5)) # Así se crea el rango de valores dentro de una lista con el nombre "c".

total2 = 0 # Defino la variable total2 con el valor de 0.

for i in c:
    total2 = total2 + i

print(total2)
print("hi")


# Ejercicio B

print( 5 % 3) # Esto lo que hace es dejar el resto de la division como resultado, por lo tanto en este caso es 2. 

total3 = 0

for z in range(1, 8):
    if z % 3 == 0: # Esto lo que va a hacer es buscar los multiplos de 3, puesto que estos de resultado en la division darán 0.
        total3 += z # Va a sumar los multiplos de 3 de la lista [1, 2, 3, 4, 5, 6, 7], los cuales son 3, 6 y lo va a asignar como valor de "total3"
print(total3)


total4 = 0

for y in range(1, 100):
    if y % 3 == 0 or y % 5 == 0: # Se puede usar el "or" para añadir mas cosas al "if".
        total4 += y


print(total4)