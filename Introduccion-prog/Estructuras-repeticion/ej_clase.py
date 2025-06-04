CANTIDAD = 2
duracion_total = 0
contador = 0
for i in range(CANTIDAD):
  playlist= input(f"ingrese el nombre de la playlist: ")
  duracion_playlist = 0
 
  for j in range(CANTIDAD):
    cancion = input(f"Ingrese nombre de la cancion: ")
    duracion = float(input("Duracion de la cancion; "))
    duracion_playlist += duracion
    duracion_total += duracion
    contador += 1
  print(f"Duracion total de la playlist{i} {duracion_playlist}")
promedio = duracion_total / contador
print(f"El promedio de la duracion es {promedio}")