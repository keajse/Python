#algoritmo para saber cuál de los 3 números es el mayor
number1 = int(input("Ingrese el número uno: "))
number2 = int(input("Ingrese el número uno: "))
number3 = int(input("Ingrese el número uno: "))

#Operadores lógicos and, or

if number1 > number2 and number1 > number3:
    print(f"El mayor de los números ingresados es {number1}")
else:
    if number2 > number1 and number2 > number3:
        print(f"El mayor de los números ingresados es {number2}")
    else:
        print(f"El mayor de los números ingresados es {number3}")
        
#else if se escribe elif       

if number1 > number2 and number1 > number3:
    print("El número 1 es el mayor")
elif number2 > number1 and number2 > number3:
    print("El número 2 es el mayor")
else:
    print("El número 3 es el mayor")