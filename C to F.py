#
#   Este es un conversor de celsius a fahrenheit, es la forma comprimida de otro modelo que hice anteriormente.
#

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print(fahrenheit)