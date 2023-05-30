"""
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
"""
import random
import string




def main():
    print("GENERADOR DE CONTRASEÑAS")
    len_pass = int(input("De cuantos caracteres quieres que sa tu contraseña entre 8 y 32 ? "))

    while 8 <= len_pass <= 32:
        characters = None
        upper_or_lower = input("Desea mayusculas? [S/N]: ")
        if upper_or_lower == "S":
            characters = string.ascii_uppercase + string.ascii_lowercase
        elif upper_or_lower == "N":
            characters = string.ascii_lowercase
        want_num = input("Deseas numeros ? [S/N]: ")
        if want_num == "S":
            characters += string.digits
        elif want_num == "N":
            characters = characters
        want_symbol = input("Deseas simbolos ? [S/N]: ")
        if want_symbol == "S":
            characters += string.punctuation
        elif want_symbol == "N":
            characters = characters

        else:
            print ("La contraseña sadd")    
            break
    
    def randomize(len_pass):
   
        password = "".join(random.choice(characters) for n in range(len_pass))
        return password
            
    passworw_random = randomize(len_pass)
    print("Su Nueva contraseña es : " + passworw_random)


if __name__ == "__main__":
    main()


