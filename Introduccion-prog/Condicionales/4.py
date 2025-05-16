num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if (num1 == num2 == num3):
    print("Los numeros son iguales")
else:
    menor = num1  
    numero = "Primero"
    if (num2 < menor):
        menor = num2
        numero = "Segundo"
    if (num3 < menor):
        menor = num3
        numero = "Tercero"   

    print("El menor de los tres números es:", menor, ". Se ingreso el ", numero)
