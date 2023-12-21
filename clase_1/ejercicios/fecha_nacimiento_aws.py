# Creame una funcion en python que calcule la edad a partir de la fecha de nacimiento

from datetime import date

def calcular_edad(fecha_nacimiento):
    today = date.today()
    edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Creame 5 casos de uso para probar la funcion

fecha_nacimiento_1 = date(1990, 1, 1) # devuelve 30 años

fecha_nacimiento_2 = date(2000, 1, 1) # devuelve 20 años

fecha_nacimiento_3 = date(2010, 1, 1) # devuelve 10 años

fecha_nacimiento_4 = date(2020, 1, 1) # devuelve 0 años

fecha_nacimiento_5 = date(2030, 1, 1) # devuelve -10 años  # Formato incorrecto

#  Generame 3 caso de uso con una fecha en milisegundos

fecha_nacimiento_milisegundos = date.fromtimestamp(1666156800)  # Fecha en milisegundos

fecha_nacimiento_milisegundos2 = date.fromtimestamp(1666156801)  # Fecha en milisegundos

fecha_nacimiento_milisegundos3 = date.fromtimestamp(1666156802)  # Fecha en milisegundos

# Imprimir resultados
print(f"Fecha de nacimiento 1: {fecha_nacimiento_1}, Edad: {calcular_edad(fecha_nacimiento_1)} años")
 
print(f"Fecha de nacimiento 2: {fecha_nacimiento_2}, Edad: {calcular_edad(fecha_nacimiento_2)} años")

print(f"Fecha de nacimiento 3: {fecha_nacimiento_3}, Edad: {calcular_edad(fecha_nacimiento_3)} años")

print(f"Fecha de nacimiento 4: {fecha_nacimiento_4}, Edad: {calcular_edad(fecha_nacimiento_4)} años")

print(f"Fecha de nacimiento 5: {fecha_nacimiento_5}, Edad: {calcular_edad(fecha_nacimiento_5)} años")


print(f"Fecha de nacimiento milisegundos: {fecha_nacimiento_milisegundos}, Edad: {calcular_edad(fecha_nacimiento_milisegundos)} años")