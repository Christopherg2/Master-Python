"""
Ejerciocio 9: Hacer un programa que pida numeros al usuario
indefinidamente hasta meter el numero 111
"""
contador = 1
while contador < 100:
    n = int(input("Introduce un numero"))

    if n == 111:
        break
    else:
        print(f"Has introcido el: {n}")
