#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

#Dividendo: 14
#Divisor: 5
#La división no es exacta.
#Cociente: 2
#Resto: 4

#Dividendo: 100
#Divisor: 10
#La división es exacta.
#Cociente: 10
#Resto: 0

dividendo = int(input("Dividendo: "))

divisor = int(input("Divisor: "))

cociente = dividendo // divisor

resto = dividendo % divisor

if resto == 0:
    print("La división es exacta.")

else:
    print("La división no es exacta.")

print(f"Cociente: {cociente}")

print(f"Resto: {resto}")