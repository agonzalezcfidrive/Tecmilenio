alumnos= ["Juan Perez", "Antonio Cázarez", "Luicía Gómez", "Maribel Estrada", "Rodolfo Martinez"]
print("lista sin ordenar: ", alumnos)
alumnos.sort()
print("lista ordenada: ", alumnos)
print("Primer alumno", alumnos[0])
nuevo_alumno = input ("ingresa el nuevo alumno")
alumnos.append(nuevo_alumno)
print(alumnos)
