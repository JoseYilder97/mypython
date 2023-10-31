m1="*"
m2=30
print(m2*m1)
print("* Bienvenidos a este programa* \n* que te dejara sin aliento. *")
print(m2*m1)
print()
nombre = input("Antes de inciar, \n ingresa tu nombre ")
print(f"Hola {nombre} a continuacion ingrese la figura que deseas hacer: ")
opc =int(input("1. Hexágono\n 2.Triangulo\n 3. Elipse\n 4. Pentágono\n 5. Paralelogramo\n"))
import math
while True:
    #Hexágono 
    if opc == 1:
        print("Seleccióno el hexágono")
        print("a. área \n p. perimetro")
        fig = input("Selecciona la operación que deas hacer: ")
        if fig == "a":
            print("Has seleciónado el área del hexágono")
            lado = float(input("Ingrese la longitud del hexágono: "))
            area = (3 * math.sqrt(3) * lado**2) / 2
            print(f"{nombre} El área del hexágono es: {area}")
        elif fig == "p":
            print("Has selecciónado el perímetro del hexágono")
            lado = float(input("Ingresa la longitud de un lado del hexágono: "))
            perimetro = lado * 6
            print("El perímetro del hexágono es:", perimetro)

        else:
            print(f"{nombre} La figura que seleccionaste no es valida")
    #Triangulo
    elif opc == 2:
        print("Seleccióno el triangulo")
        print("a. área \n p. perimetro")
        fig = input("Selecciona la operación que deas hacer: ")
        if fig == "a":
            print("Has seleciónado el área del triangulo")
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
            print(f"{nombre} El área del triangulo es: {area}")
        elif fig == "p":
            print("Has selecciónado el perímetro del triangulo")
            lado1 = float(input("Ingrese la longitud del primer lado: "))
            lado2 = float(input("Ingrese la longitud del segundo lado: "))
            lado3 = float(input("Ingrese la longitud del tercer lado: "))
            perimetro = lado1 + lado2 + lado3
            print(f"El perímetro del triangulo es: {perimetro}")
        else:
            print(f"{nombre} La figura que seleccionaste no es valida")
    #Elipse
    elif opc == 3:
        print("Seleccióno el elipse")
        print("a. área \n p. perimetro")
        fig = input("Selecciona la operación que deas hacer: ")
        if fig == "a":
            print("Has seleciónado el área del elipse")
            a = float(input("Ingrese el valor del semieje mayor (a): "))
            b = float(input("Ingrese el valor del semieje menor (b): "))
            area = math.pi * a * b
            print(f"{nombre} El área del elipse es: {area}")
        elif fig == "p":
            print("Has selecciónado el perímetro del elipse")
            a = float(input("Ingrese el valor del semieje mayor (a): "))
            b = float(input("Ingrese el valor del semieje menor (b): "))
            perimetro = 2 * math.pi * math.sqrt((a**2 + b**2) / 2)
            print(f"El perímetro del elipse es: {perimetro}")

        else:
            print(f"{nombre} La figura que seleccionaste no es valida")
    elif opc == 4:
        print("Seleccióno el pentágono")
        print("a. área \n p. perimetro")
        fig = input("Selecciona la operación que deas hacer: ")
        if fig == "a":
            print("Has seleciónado el área del pentágono")
            lado = float(input("Ingrese la longitud del lado del pentágono: "))
            apotema = float(input("Ingrese la apotema del pentágono: "))
            area = (5 * lado * apotema) / 2
            print(f"{nombre} El área del pentágono es: {area}")
        elif fig == "p":
            print("Has selecciónado el perímetro del pentágono")
            lado = float(input("Ingrese la longitud del lado del pentágono: "))

            perimetro = 5 * lado
            print(f"El perímetro del pentágono es: {perimetro}")

        else:
            print(f"{nombre} La figura que seleccionaste no es valida")
    elif opc == 5:
        print("Seleccióno el paralelogramo")
        print("a. área \n p. perimetro")
        fig = input("Selecciona la operación que deas hacer: ")
        if fig == "a":
            print("Has seleciónado el área del paralelogramo")
            base = float(input("Ingrese la longitud de la base del paralelogramo: "))
            altura = float(input("Ingrese la altura del paralelogramo: "))
            area = base * altura
            print(f"{nombre} El área del paralelogramo es: {area}")
        elif fig == "p":
            print("Has selecciónado el perímetro del paralelogramo")
            lado1 = float(input("Ingrese la longitud del primer lado: "))
            lado2 = float(input("Ingrese la longitud del segundo lado: "))
            perimetro = 2 * (lado1 + lado2)
            print(f"El perímetro del paralelogramo es: {perimetro}")

        else:
            print(f"{nombre} La figura que seleccionaste no es valida")