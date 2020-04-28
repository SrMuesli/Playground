d = {}
# d = {"George": 24, "Tom": 32}  Un diccionario puede crearse así.

d["George"] = 24
d["Tom"] = 32       # O también se puede crear cada parte de el de una en una.
d["Jenny"] = 16

print(d["George"])  # Con esto lo que se hace es imprimir el valor que corresponde a la palabra "George" del diccionario "d".ArithmeticError

d[10] = 300         # Los diccionarios pueden crearse con palabras o numeros, por lo que en este caso al numero "10" le corresponde el valor "300".

print(d[10])

for key, value in d.items():
    print("Key") 
    print(key)     # Esto imprime el objeto del diccionario.
    print("Valor")
    print(value)   # Esto imprime el valor de dicho objeto.


for key, value in d.items():
    print("Key:")  # Al poner 2 puntos en esto.
    print(key)     
    print("Valor:")
    print(value)   
    print("")      # Y añadir esto, queda mas cuco. No se por que.