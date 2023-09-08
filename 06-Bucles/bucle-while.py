"""
# Bucle while 
 Estructura de control que itera o repite la ejecución de una serie de
 instruciones tantas veces como sea necesario, hasta que deje de 
 cumplirse la condición
 
 while condicion:
 bloque de instrucines
 actualizacion del contador 
	"""
""" 
contador = 1
while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1
"""
print("-------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + "," + str(contador)
    contador += 1

print(muestrame)
