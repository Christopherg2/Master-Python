"""""
#Ejecicio 10. El programa tiene que pedir la nota de 15 estudiantes
y sacar por pantalla cuantos han aprovado y reprobado 
"""""

contador = 1

aprovados = 0
suspendidos = 0
n_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= n_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno {contador}\" ? "))
    if nota >= 5:
        aprovados + 1
    else:
        suspendidos += 1

    contador += 1

print(f"\n Alumnos aprovados: {aprovados}")
print(f" Alumnos suspedindos: {suspendidos}")
