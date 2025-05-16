num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if ((num1 + num2) > (num1**2 - num2**2) ):
    prom = (num1 + num2) / 2
    print (prom)
else:
    print("No cumple")