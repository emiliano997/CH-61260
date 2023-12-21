# Creame una función que reciba grados Celsius y los convierta a Fahrenheit.

def celsius_to_fahrenheit(celsius):
    """
    Convertir grados Celsius a Fahrenheit

    Args:
        celsius (float): Grados Celsius

    Returns:
        float: Grados Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Creame 5 casos de prueba para probar la función

print(celsius_to_fahrenheit(0)) # 32

print(celsius_to_fahrenheit(100)) # 212

print(celsius_to_fahrenheit(-40)) # -40

