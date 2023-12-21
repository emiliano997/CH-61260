from datetime import datetime

def calcular_edad(fecha_nacimiento_str):
    try:
        # Intentar convertir la cadena de fecha a un objeto datetime
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d')
    except ValueError:
        # Capturar el error en caso de formato incorrecto
        print("Error: El formato de la fecha es incorrecto. Utiliza el formato 'YYYY-MM-DD'.")
        return None
    
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Casos de uso con posibles errores en el formato de fecha
fecha_nacimiento_1 = "1990-01-01"
fecha_nacimiento_2 = "1985-05-15"
fecha_nacimiento_3 = "2000-10-30"
fecha_nacimiento_4 = "1975-03-08"
fecha_nacimiento_5 = "30-10-2000"  # Formato incorrecto

edad_persona_1 = calcular_edad(fecha_nacimiento_1)
edad_persona_2 = calcular_edad(fecha_nacimiento_2)
edad_persona_3 = calcular_edad(fecha_nacimiento_3)
edad_persona_4 = calcular_edad(fecha_nacimiento_4)
edad_persona_5 = calcular_edad(fecha_nacimiento_5)  # Esto generará un error y mostrará el mensaje

# Imprimir resultados
print(f"Fecha de nacimiento 1: {fecha_nacimiento_1}, Edad: {edad_persona_1} años")
print(f"Fecha de nacimiento 2: {fecha_nacimiento_2}, Edad: {edad_persona_2} años")
print(f"Fecha de nacimiento 3: {fecha_nacimiento_3}, Edad: {edad_persona_3} años")
print(f"Fecha de nacimiento 4: {fecha_nacimiento_4}, Edad: {edad_persona_4} años")
print(f"Fecha de nacimiento 5: {fecha_nacimiento_5}, Edad: {edad_persona_5}")  # Aquí mostrará el mensaje de error
