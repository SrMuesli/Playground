# Este es un loop infinito, porque por cada item de la lista, añade 1 a la lista.
# Si esto ocurre el programa no terminara de ejecutarse, porque el final es el infinito.
# Para detener un loop infinito, hay que pulsar las teclas "Control + C"


my_favorite_numbers = [4, 8, 15, 16, 42]

for number in my_favorite_numbers:
  my_favorite_numbers.append(1)