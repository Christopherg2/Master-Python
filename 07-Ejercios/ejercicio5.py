n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

if n1 < n2:

    for contador in range(n1, n2 + 1):
        print(contador)
    else:
        print("El numero uno debe ser menor al segundo")
