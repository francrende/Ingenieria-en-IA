monto = float(input("Ingrese el monto: "))

if monto > 50000:
    desc = monto * 0.8
    print("El monto queda en:", desc)
elif monto > 25000:
    desc = monto * 0.85
    print("El monto queda en:", desc)
elif monto > 15000:
    desc = monto * 0.95
    print("El monto queda en:", desc)
else:
    print("Tu compra no tiene descuento: ", monto)
