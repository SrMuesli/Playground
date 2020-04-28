# BMI Calculator

name1 = "Willyrex"
height_m1 = 2           # Este es el primer sujeto
weight_kg1 = 90

name2 = "Vegetta777"
height_m2 = 1.9         # Este es el segundo sujeto
weight_kg2 = 70

name3 = "Knekro"
height_m3 = 1.75        # Este es el tercer sujeto
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg): # Con esto el "argument" va a ser name, pero depende de como "apellide" llamará a una variable u otra.
    bmi = weight_kg / (height_m **2)
    #print("bmi: ")
    #print(bmi)
    if bmi < 25:
        return name + " bmi is " +  str(bmi) + " so is not overweight"
    else:
        return name + " bmi is " + str(bmi) + " so is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1) # Asigna a la variable "result1" el calculo del sujeto 1.
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)