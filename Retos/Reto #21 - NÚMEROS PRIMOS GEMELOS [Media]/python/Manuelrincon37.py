"""/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */"""

def is_prime(number)-> bool:
    if number <= 1:
        return False
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def find_prime_twins(range_number: int):
    for i in range(2,range_number):
        if i + 2 < range_number and is_prime(i) and is_prime(i + 2):
            print(f"({i}, {i + 2})")

find_prime_twins(60)


