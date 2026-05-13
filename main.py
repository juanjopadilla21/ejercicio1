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

    # Condicionales
    if promedio >= 4.5:
        notafin = "Excelente"
    elif promedio >= 3.5:
        notafin = "Aprobado"
    else:
        notafin = "Reprobado"

    # Mostrar resultados
    print("Resultado")
    print("Estudiante:", nombre)
    print("Promedio:", promedio)
    print("Estado:", notafin)

    # Bucle while para varios estudiantes
    siguente = input("¿Desea ingresar otro estudiante? (si/no): ")

print("HASTA LUEGO :)")