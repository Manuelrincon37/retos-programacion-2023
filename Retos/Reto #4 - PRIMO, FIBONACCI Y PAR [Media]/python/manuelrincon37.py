"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */"""

def checknum(n):
    check_pair = "es par, " if is_pair(n) else "no es par, "
    check_prime = "es primo, " if is_prime(n) else "no es primo, "
    check_fibo = "Es fibo" if is_fibo(n) else "no es fibo"
    print("el numero {}, {} {} y {}".format(n,check_pair,check_prime,check_fibo))
    

def is_pair(n) -> False:
    if n%2 == 0:
        return True
    else: return False

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(12))

def is_fibo(n)-> bool:
    a, b = 0, 1
    while a < n:
     a, b = b, a + b
    return a == n


checknum(45)