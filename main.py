# Sistema de Calificaciones
siguente = "si"

while siguente == "si":

    # Entrada de datos
    nombre = input("Ingrese el nombre del estudiante: ")

    suma = 0
 # Bucle for para las 5 notas
    for i in range(1, 6):

        # Mensaje para contador
        nota = float(input("Ingrese nota " + str(i) + ": "))

        # Validar que la nota esté entre 1.0 y 5.0
        while nota < 1.0 or nota > 5.0:
            print("Error. La nota debe estar entre 1.0 y 5.0")
            nota = float(input("Ingrese nuevamente la nota " + str(i) + ": "))

        suma = suma + nota

    # Cálculo del promedio
    promedio = suma / 5

