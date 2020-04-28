name = "Juan"
heigh_m = 2
weight_kg = 90

bmi = weight_kg / (heigh_m ** 2) #BMI es igual al peso dividido entre la altura al cubo
print("bmi: ")
print(bmi)
if bmi < 25: # Si el BMI es menor de 25
    print(name)
    print("is not overweight")
else: # El BMI no es menor de 25
    print(name)
    print("is overweight")