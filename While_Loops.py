# While Loops


total = 0
for x in range(1, 5): # Esto es un For Loop.
    total += x
print(total)


total2= 0       # Este es un While Loop
z = 1           # Tenemos que definir la variable que va a medir el While, puesto que esto no crea sino la lista.
while z < 5:    # Mientras "z" sea menor que 5, se van a ejecutar las siguientes lineas.
    total2 += z # Sumar el valor de "z" a la variable "total2"
    z += 1      # Añadir cada loop que se haga el valor 1 a "z". Por lo tanto cada vez que sea "z" menor que 5, sumará 1 a "z". 1,2,3,4.
print(total2)

#______________________________________________________________________________________________________________________________________________________________________________
# Ejercicio 2 "While"
#
# En este ejercicio lo que se hace es sumar los valores positivos que hay en la lista, el LOOP parará cuando encuentre un numero negativo.
# 
# Si la lista no tiene valores negativos, no funcionará puesto que sumará sin parar a la variable "i",
# hasta que de error puesto que el numero sea mas grande que la cantidad de numeros que hay en la lista.

given_list = [5, 4, 4, 3, 1, -2, -3, -5] # Vamos a sumar los digitos positivos de esta lista. 

total3 = 0                  # Define la variable que nos va a dar el resultado.
i = 0                       # Define la variable que vamos a usar para "movernos" por la lista, puesto que al sumarle +1, pasaremos al siguiente numero de la lista indexada.
while given_list[i] > 0:    # Esto hace que se ejecute lo siguiente si el numero es MAYOR de 0.
    total3 += given_list[i] #Si el numero es mayor, lo suma al "total3".
    i += 1                  # Y va a sumar 1 a la variable "i" para así seguir comprobando los numeros de la lista.
print(total3)

# Para que funcione sin numeros negativos se puede añadir el condicionante "lenght" de la siguiente forma:
#  
#   while i < len(given_list) and given_list[i] > 0:
#       total3 += given_list[i]
#       i += 1          
#        
# Con ello lo que hacemos es indicar que mientras el valor de i no sea mayor que la longitud de la lista, y que el numero no sea menor de cero, ejecutará el programa.

#______________________________________________________________________________________________________________________________________________________________________________
# Ejercicio 2 "For"

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]

total4 = 0
for element in given_list2:
    if element <= 0:          # Este codigo lo que hace es parar el loop si el elemento es igual o menor de 0, puesto que sino el loop iba a sumar los numeros negativos.
        break                 # El codigo parará por lo que si hay algun numero positivo despues, este no se va a contar.
    total4 += element
print(total4)

#______________________________________________________________________________________________________________________________________________________________________________
# Ejercicio 2 -- Otra forma mas de hacerlo

given_list3 = [5, 4, 4, 3, 1, -2, -3, -5,]
total5 = 0
y = 0

while True:                     # Mientras sea cierto "True" se ejecuta lo siguiente.
    total5 += given_list3[y]    # Se le suma a la variable "total5" el valor de la lista que corresponda con el index que proporciona la variable "y".
    y += 1                      # Esto le suma 1 a la variable de index "y" para así avanzar por la lista.
    if given_list3[y] <= 0:     # Esto va a detener el LOOP tan pronto como se encuentre con un valor en negativo en la lista, puesto que si es menor/igual que 0 ejecuta el "break".
        break
print(total5)

#______________________________________________________________________________________________________________________________________________________________________________
# Ejercicio prueba -- Hay que sumar los numeros negativos.

given_list5 = [9, 7, 5, 4, 4, 3, 1, -2, -3, -5, -7, -9]
total6 = 0
k = 0

while k < len(given_list5):         # Mientras que la variable "k" sea menor que la longitud de la lista hace lo siguiente:
    if given_list5[k] <= 0:         # Si el numero de la lista con el index "k" es menor de 0:
        total6 += given_list5[k]    # Suma el valor a total6.
    k += 1                          # Esto lo que hace es sumar 1 al valor de index hasta que se termine de ejecutar el "while".

print(total6)

# Solución que da el teacher:

given_list6 = [9, 7, 5, 4, 4, 3, 1, -2, -3, -5, -7, -9]
total7 = 0
j = len(given_list6) - 1        # El usa esto para que así el numero base que busca el index en lugar de 0 sea -1 y así empieze por el final de la lista, así no hay que comprobar todos los numeros anteriores.
while given_list6[j] < 0:       # por lo que se "invierte" el funcionamiento, y tan pronto como encuentre un numero positivo, el script parará.
    total7 += given_list6[j]
    j -= 1
print(total7)
