"""
 #EJERCICIO 8
 # Programa, ¿Cuanto es el x numero? dado por el usuario_
	"""
n1 = int(input("Por favor introduce un número : "))
porcentaje = int(input(f"¿Que porcentaje quieres sacar de {n1} ?"))

operacion = (n1 * (porcentaje/100))
print(f"El {porcentaje}% de {n1} es : {operacion}")
