nombre = "Christopher"

# Funciones generales
print(type(nombre))
# Ver el tipo de la variable

# Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    # cuando no se pone operadpdes el if por default da valor true
    print("Esa variables es un string")
else:
    print("No es un string")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limíar espación

frase = "   xd   :vuwu   "
print(frase)
print(frase.strip())
# funcion strip, metodo que limpia los espacios


# Eliminar variables

year = 2023
print(year)
del year
# print(year)
# con del elimina la variable, marcada error porque ya no existe
# se puede aplicar con indices.

# Comprobar variable vacio

texto = "xdxd"
if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido:", len(texto))
# Funcion len, puede ver cuantos caracteres tiene una variable, lista


# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

# metodo .find para buscar

# demplazar palabras en un strig

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# MAYUSCULAS y minisculas
print(nombre)
print(nombre.lower())  # pasar a minisculas
print(nombre.upper())  # pasar a mayusculas
