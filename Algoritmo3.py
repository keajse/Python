#Un profesor necesita obtener el nombre de cada estudiante y sus 5 respectivas notas y debe mostrar la lsta de los estudiantes con su respectiva nota final.

names = []
grades = []

while True:
    names.append(input("ingrese el nombre del estudiante: "))
    average= 0
    for i in range(1,6):
        average += float(input(f"Ingrese la nota {i}: "))
    average = average/5
    grades.append(average)
    stopProgram = input("Desear para el programa (s- Si, otra tecla no)")
    if stopProgram == "s" or stopProgram == "S":
        break
for j in range(len(names)):
   lista = {
       "Nombre: ": names[j],
       "Promedio: ": grades[j]
   }
   print(lista)