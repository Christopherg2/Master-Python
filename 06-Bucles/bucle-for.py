"""
#FOR  
for varibale in elemento iterable  (lista, rango, etc)
  BLOQUE DE INSTRUCIONES
"""

"""
contador = 0
resultado = 0
#Inicializamos la variable con el valor 0

for contador in range(0, 10):
    print("Voy por el " + str(contador))

    resultado += contador
   # resultado = resultado + contador

print(f"El resultado es: {resultado}")
"""

# EJEMPLO TABLAS DE MULTIPLICAR

print("\n*** EJEMPLO ***")
numero_usuario = int(input("¿De que numero quieres ver la tabla?  "))
# Transforma el tipo strin a entero con int() antes del input

if numero_usuario < 1:
    numero_usuario = 1

print(f"\nTabla de multiplicar del numero {numero_usuario} ")

for numero_tabla in range(1, 11):

    if numero_usuario == 45:
        print("Nose puede multiplicar numeros prohibidos !!!")
        break
    # Con break se rompe el ciclo, se sale, se cierra.

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla} ")

else:
    print("Tabla finalizada.")
