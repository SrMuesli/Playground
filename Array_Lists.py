# Listas en Python.


a = [3, 10, -1]   # Crea la lista "a" con los datos de dentro del corchete

print(a)

a.append(8)   # .append es para Adjuntar lo del parentesis a la lista "a".

print(a)

a.append("Hello world")   # También se puede añadir Strings dentro de las listas.

print(a)

a.append([15, 413])   # Se pueden añadir mas listas dentro de una lista.

print (a)

a.pop()   # El .pop elimina el ultimo objeto de la lista.

print(a)

print(a[0])   # Esto llama a un objeto en concreto de la lista. Usa el numero index 0, el cual es el primero de la lista.

print(a[2])   # Esto llama al objeto 2 de la lista, el cual en realidad es el tercero.

a[0] = 10000   # Esto se usa para cambiar un valor de la lista por otro. Por lo tanto el objeto indexado 0 a partir de ahora va a tener el valor de "1000".

print(a[0])

# Lista B
# Cambiar datos de lugar


# Forma lenta y con mucho codigo.

b = ["banana", "apple", "microsoft"] # Crea la lista de objetos.
print(b)
temp = b[0] # Asigna el valor "banana" a la variable "temp".
b[0] = b[2] # Cambia el valor de "banana" por el de "microsoft".
b[2] = temp # Cambia el valor de "microsoft" por el que tiene temp, el cual es "banana".

print(b)


# Forma rapida y con poco codigo.
f = ["cardamomo", "vinagre", "sangría"]
print (f)

f[0], f[2] = f[2], f[0] # Esto dice que los valores originales de "0 y 2" van a ser los de "2 y 0"

print(f)


print("Mameluco")