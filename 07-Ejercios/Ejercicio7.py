"""
 #Ejercicio 7 
 Programa que muestre todos los numeros impares entre dos números 
 que decida el usuario_
	"""

n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

if n1 < n2:
    for x in range(n1, (n2 + 1)):
        if x % 2 == 0:
            print(f"{x} es PAR")
        else:
            print(f"{x}es IMPAR")
else:
    print("El numero 1 debe ser mayor al 2")
