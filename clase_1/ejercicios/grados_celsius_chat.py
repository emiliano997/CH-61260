def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

grados_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
grados_fahrenheit = celsius_a_fahrenheit(grados_celsius)
print(f"{grados_celsius} grados Celsius son equivalentes a {grados_fahrenheit:.2f} grados Fahrenheit.")
