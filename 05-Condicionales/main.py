# Estructura de control que permite controlar el flujo del programa

# Condicional IF
# Si se_cumple_esta_condición:
#    Ejecutar grupo de instruciones
#   SI NO
#  Se ejecuta otro grupo de instruciones

# if condición:
#    instruciones:
# else:
#   otras instruciones

# EJEMPLO   1
print("EJEMPLO 1")

"""" color = "rojo"

 color = input("Adivina cual es mi color favorito?:")
 if color == "negro":
  print("En ahora buena has adivinado")
  print("El color es negro")
 else:
  print("Color incorrecto")
"""

# EJEMPLO2

print("EJEMPLO 2")

# year = int(input("¿En que año estamos?"))
# if year >= 2021:
#   print("Estamos de 2021 en adelante")
# else:
#   print("Es un año anterior a 2021")


# EJEMPLO 3

print("EJEMPLO 3")
"""""
nombre = "Chirs"
cuidad = "Mexico"
continente = "America"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")

    if continente != "America":
        print("El usuario no Americano")
    else:
        print(f"Es amaricano y de {cuidad}")

else:
    print(f"{nombre} NO es mayor de edad")
    """


# EJEMPLO 4

print("EJEMPLO 4")
"""dia = int(input("Introduce el numero del dia de la semana"))


if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana :3") 
                    """

"""
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana ")
  """

# EJEMPLO 5

print("EJEMPLO 5")
""" edad_minima = 18
edad_maxima = 65
edad_of = int(input("Introduce tu edad?"))

if edad_of >= 18 and edad_of <= 65:
    print("Estas listo para chambear !!!")
else:
    print("Te falta edad para chambear ")"""

# Operadores logicos
""" and y 
or  or
!negación 
not no """

# EJEMPLO 6

print("EJEMPLO 6")
"""pais = "España"
if pais == "Colombia" or pais == "España" or pais == "Peru":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"{pais} NO es un país de habla hispana")
     """


# EJEMPLO 7

print("EJEMPLO 7")
"""
pais = "Mexico"
if not (pais == "Mexico" or pais == "España" or pais == "Peru"):
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} Si es un país de habla hispana")
 """
# EJEMPLO 8

print("EJEMPLO 8")
pais = "Colombia"
if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un país de habla hispana")
else:
    print(f"{pais} Si es un país de habla hispana")

 # SOY DE MÉXICO :"3
