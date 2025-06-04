desc = 0
cant = 5
cant_101 = 0
valor_101 = 0

cant_mult_7 = 0


for i in range(cant):
    valor = int(input("Ingrese un valor: "))
    # Verifico
    while (valor % 2 != 0):
        # Si es el primer descartado, guardo valor minimo
        if (desc == 0):
            min = valor
        # Si el valor es el min, lo actualizo
        if (valor < min):
            min = valor
        valor = int(input("Ingrese un valor valido: "))
        desc += 1

    # Actualizo variables de cantidad de num mayores a 101 
    if (valor > 101):
        cant_101 += 1
        valor_101 += valor
    
    # Calculo de maximo
    if (i == 0):
        mayor = valor

    if (valor > mayor):
        mayor = valor

    if (valor % 7 == 0): 
        for j in range(valor):
            mult_7 = int(input("Ingrese un numero a sumar: "))
            cant_mult_7 += mult_7


if (desc > 0):
    print ("Cant valores descartados: ", desc)
    print ("Menor valor descartado: ", min)
else:
    print ("No se descartaron numeros")

if (cant_101 > 0):
    print ("El promedio de los valores mayores a 101 es: ", valor_101/cant_101)

print ("El mayor de los ingresados es: ", mayor)

print ("La sumatoria de la cantidad de valores ingresados en correspondencia con el numero multiplo de 7 es: ", cant_mult_7)



