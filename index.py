m1="*"
m2=30
print(m2*m1)
print("* Bienvenidos a este programa* \n* que te dejara sin aliento. *")
print(m2*m1)
print()
n = input("Antes de inciar, \n ingresa tu nombre ")
n = n.upper()
print("""a = suma,
b = resta,
c = multiplicación,
d = división,
e = división entera
f = división resto,
g = binario,
h = octal,
i = hexadecimal,
j = no disponible
k = no programada""")
def suma():
    n1 = int(input("Ingrese el primer valor a sumar: "))
    n2 = int(input("Ingrese el segundo valor a sumar: "))
    r = n1 + n2
    print("El resultado de la suma es: ", r)
 
def resta():
    n1 = int(input("Ingrese el primer valor a restar: "))
    n2 = int(input("Ingrese el segundo valor a restar: "))
    r = n1 - n2
    print("El resultado de la resta es: ", r)
def mult():
    n1 = int(input("Ingrese el primer valor a multiplicar: "))
    n2 = int(input("Ingrese el segundo valor a multiplicar: "))
    r = n1 * n2
    print("El resultado de la multiplicación es: ", r)
def division():
    n1 = int(input("Ingrese el primer valor a divisor: "))
    n2 = int(input("Ingrese el segundo valor a dividendo: "))
    r = n1 / n2
    print("El resultado de la división es: ", r)
def binario():
    n1 = int(input("Ingese el número que desea convertir a binario: "))
    r = bin(n1)
    print("El número ",n1, " pasado a binario, es: ", r)
def octal():
    n1 = int(input("Ingese el número que desea convertir a octal: "))
    r = oct(n1)
    print("El número ",n1, " pasado a octal, es: ", r)
def hexadecimal():
    n1 = int(input("Ingese el número que desea convertir a hexadecimal: "))
    r = hex(n1)
    print("El número ",n1, " pasado a hexadecimal, es: ", r)
 
while True:
    opc = input(f" {n} seleccione la letra correspondiente \n a la operación que desea ejecutar \n (o 's' para salir): ")
    print()
    if opc == "s":
        break
    elif opc == "a":
        suma()
    elif opc == "b":
        resta()
    elif opc == "c":
        mult()
    elif opc == "d":
        division()
    elif opc == "g":
        binario()
    elif opc == "h":
        octal()
    elif opc == "i":
        hexadecimal()
    else:
        print(f"{n} La opción seleccionada no es válida. Por favor, seleccione otra opción.")