import math
# este es para calcular el area y perimetro de un elipse
def calcular_area_elipse(a, b):
    area = math.pi * a * b
    return area

def calcular_perimetro_elipse(a, b):
    perimetro = 2 * math.pi * math.sqrt((a**2 + b**2) / 2)
    return perimetro

semieje_mayor = int(input('Ingrese el semieje mayor: '))
semieje_menor = int(input('Ingrese el semieje memor: '))

area = calcular_area_elipse(semieje_mayor, semieje_menor)
perimetro = calcular_perimetro_elipse(semieje_mayor, semieje_menor)

print("El área de la elipse es:", area)
print("El perímetro de la elipse es:", perimetro)

#como hallar el area y perimetro de un hexágono


lado = float(input("Ingrese la longitud de un lado del hexágono: "))

area = (3 * math.sqrt(3) * lado**2) / 2
perimetro = lado * 6

print("El área del hexágono es:", area)
print("El perímetro del hexágono es:", perimetro)



# pentágono

lado = float(input("Ingresa la medida de un lado del pentágono: "))

perimetro = 5 * lado
apotema = lado / (2 * math.tan(math.pi/5))
area = (perimetro * apotema) / 2

print("El perímetro del pentágono es: ", perimetro)
print("El área del pentágono es: ", area)

#paralelogramo

def calcular_paralelogramo(base, altura, lado): 
    perimetro = 2 * lado + base 
    area = base * altura 
    return perimetro, area 
 
base = float(input("Ingresa la medida de la base del paralelogramo: ")) 
altura = float(input("Ingresa la medida de la altura del paralelogramo: ")) 
lado = float(input("Ingresa la medida de uno de los lados del paralelogramo: ")) 
 
perimetro, area = calcular_paralelogramo(base, altura, lado) 
 
print("El perímetro del paralelogramo es:", perimetro) 
print("El área del paralelogramo es:", area)

#trisngulo
def calcular_perimetro(base, lado):
    perimetro = 2 * lado + base
    return perimetro

def calcular_area(base, altura):
    area = base * altura
    return area

base = float(input("Ingresa la medida de la base del paralelogramo: "))
altura = float(input("Ingresa la medida de la altura del paralelogramo: "))
lado = float(input("Ingresa la medida de uno de los lados del paralelogramo: "))

perimetro = calcular_perimetro(base, lado)
area = calcular_area(base, altura)

print("El perímetro del paralelogramo es:", perimetro)
print("El área del paralelogramo es:", area)