def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si encuentra un divisor, el número no es primo

    return True  # Si no encuentra divisores, el número es primo

# Ejemplos de uso:
numero1 = 11
numero2 = 25

if es_primo(numero1):
    print(f"{numero1} es un número primo.")
else:
    print(f"{numero1} no es un número primo.")

if es_primo(numero2):
    print(f"{numero2} es un número primo.")
else:
    print(f"{numero2} no es un número primo.")