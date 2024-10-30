#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. 
# En caso que sea letra, determine si es mayúscula o minúscula.

#Ingrese caracter: 9
#Es numero.
#Ingrese caracter: A
#Es letra mayúscula.
#Ingrese caracter: f
#Es letra minúscula.
#Ingrese caracter: #
#No es letra ni número.

caracter = input("Ingrese carácter: ")

if caracter.isalpha():

    if caracter.isupper():
        print("Es letra mayúscula.")

    else:
        print("Es letra minúscula.")

elif caracter.isdigit():
    print("Es número.")

else:
    print("No es letra ni número.")