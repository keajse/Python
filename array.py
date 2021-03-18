#myArray = [2, "hola", 2.5,] #tamaño 3 pero en index es 0 - 2

#recorrer un arreglo

#option one

#for i in range(0,3):
   #print(myArray[i])

#option two

#for i in range(len(myArray)):
    #print(myArray[i])

#option three tipo forech

#for i in myArray:
    #print(i)

#agrega un nuevo elemento al final de la lista append
#myArray.append("Maria Camila")
#print(myArray)

#remove elimina el primer dato que encuentre relacionado con lo ingresado en los parentesis. Remove
#myArray.remove(2.5)
#print(myArray)

#invertir un arreglo .reverse
#myArray.reverse()
#print(myArray)

#para ordenar de menor a mayor sort
myArray=[7,8,2,1]
myArray.sort()
print(myArray)

#insertar en determinada posición
myArray.insert(0, 12)
print(myArray)