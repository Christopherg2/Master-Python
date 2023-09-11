"""
Funciones: 
Una función es es un conjunto de intrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando 
a la función tantas veces como sea necesario.

def nombreDeMiFunción(parametros):
   #BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)
 
"""
"""
# Ejemplo 1
print("EJEMPLO 1")


def muestra_nombres():
    print("Chris")
    print("Dylan")
    print("Silvia")
    print("\n")


# Invocar funcion
muestra_nombres()
"""
"""
# Ejemplo 2
print(" ### EJEMPLO 2 ### ")


def mostrarnombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad")
    else:
        print("Y  NO eres mayor de edad")


nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarnombre(nombre, edad)
# mostrarnombre("Dylan")
# mostrarnombre("Silvia")
"""

# Ejemplo 3
print(" ### EJEMPLO 3 ### ")

"""
def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")
    for contador in range(11):
        operación = numero*contador
        print(f"{numero} x {contador} = {operación }")

    print("\n")


tabla(3)
tabla(8)
tabla(9)

# Ejemplo 3.1
print(" ---------------- ")
print(" ### EJEMPLO 3.1 ### ")

for numero_tabla in range(1, 11):
    tabla(numero_tabla)
    """

# Ejemplo 4
# Parametros opcionales
""" Parametro opcional, se le otorga un valor por defecto
dentro de la función
"""

print(" ---------------- ")
print(" ### EJEMPLO 4 ### ")

"""
def getempleado(nombre, dni=None):

    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DNI:{dni}")
    if dni != None:
        print(f"DNI: {dni}")


getempleado("Christopher Web", 17620098)
"""

print(" ---------------- ")
print(" \n  # EJEMPLO 5 ### ")
# Parametros opcionales y return o devolver datos
"""

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo


print(saludame("Christopher G"))
"""

print(" ---------------- ")
print(" \n### EJEMPLO 6 ### ")
"""

def calculadora(n1, n2, basicos=False):

    suma = n1+n2
    resta = n1-n2
    multi = n1*n2
    división = n1/n2

    cadena = ""
    if basicos != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(división)

    return cadena


print(calculadora(56, 5,))

"""
print(" ---------------- ")
print(" \n### EJEMPLO 7 ### ")
# Como usar funciones dentro de otras funciones


def getnombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getapellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto


def devulvetodo(nombre, apellidos):
    texto = getnombre(nombre) + "\n" + getapellidos(apellidos)
    return texto


print(devulvetodo("Christopher", "Garcia Garcia"))
