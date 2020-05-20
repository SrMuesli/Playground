# More About Loops

a = ["platanos", "camisetas", "comunismo"]

for element in a:       # Por cada elemento de "a" imprimir elemento.
    print(element)


for i in range(3):       
    print(a[i])

for s in range(len(a)):
    print(a[s])


for k in range(len(a)):
    for j in range(k + 1):
        print(a[k])