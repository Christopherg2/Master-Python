# Script que muestre por pantalla todos los números pares del 1 al 120.

# contador = 1  # Creamos la variable y la inicializamos con el valor 1
# Tambien mencionar que en python, se declar y inializar al principio, sino hasta el ciclo

for contador in range(1, 121):  # eL Contador se iniziliza, se crea un rango para los
    # numeros pales

    if contador % 2 == 0:
        print(contador)

    """else:
        print(f"{contador} Es impar")
        """
"""_
 el for recorre cada numero del rango, cada numero recorrido lo guarda en la variable
 contador, el numero se divide entre dos y si el resultado es igual igual a 0 s
 se muestra, esa es la formula para saber si es par. 
 """
