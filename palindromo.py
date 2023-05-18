def palindromo(palabra):
    palabra = palabra.replace(" ", "")   
    palabra = palabra.lower()
    palabra_invertida = palabra[: : -1]
    if palabra == palabra_invertida:
        return (True)
    
def run():
    palabra = input("Escriba una palabra: ")
    if palindromo(palabra):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

#Lo siguiente es un 'Entry Point'. Es un estándar de Python para dar inicio a un programa.
if __name__ == "__main__":
    run()
