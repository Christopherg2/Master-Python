"""
Variables locales:Se definen dentro de una función y no se puede 
usar fuera de ella, solo están disponibles dentro,
a no ser que hagamos un return

Variables globales: Son las que se declaran fuera de la función 
y estan disponibles dentro y fuera de ellas
"""
# Variables global
frase = "Hola mundo de chris que tal el dia"

print(frase)
print("Var global, externo de la funcón")

print(" ---------------- ")


def heymundo():
    frase = "Bomnoche Chris!!"  # var local dentro de la funcion
    print("Var local, dentro de la funcón")
    print(frase)

    year = 2023
    print(year)

    global website
    # Hacer una variable global
    website = "Christopherweb.mx"
    print("DENTRO:", website)

    return "Dato revuelto" + str(year)


print(heymundo())
print("Fuera", website)
