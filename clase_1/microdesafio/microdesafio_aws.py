# Crear una funcion para saber si un numero es primo o no

def esPrimo(numero):
    if numero == 1:
       return False
    for i in range(2, numero):
       if numero % i == 0:
           return False
    return True


# Prueba de la funcion con numeros estaticos

print(esPrimo(1)) # False

print(esPrimo(2)) # True

print(esPrimo(3)) # True

print(esPrimo(4)) # False