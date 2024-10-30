#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.

#El programa debe recibir como entrada 2 números reales y un operador, que puede ser +, -, * o /.

#La salida del programa debe ser el resultado de la operación.

#Operando: 3
#Operador: +
#Operando: 2
#3 + 2 = 5
#Operando: 6
#Operador: -
#Operando: 7
#6 - 7 = -1
#Operando: 4
#Operador: *
#Operando: 5
#4 * 5 = 20
#Operando: 10
#Operador: /
#Operando: 4
#10 / 4 = 2.5
#Operando: -1
#Operador: **
#Operando: 4
#-1 ** 4 = 1

def calcular(operando1, operador, operando2):

    if operador == '+':
        return operando1 + operando2
    elif operador == '-':

        return operando1 - operando2
    elif operador == '*':

        return operando1 * operando2
    elif operador == '/':
        
        if operando2 != 0:  
            return operando1 / operando2

        else:
            return "Error: División por cero."

    else:
        return "Error: Operador no válido."



while True:

    try:
        operando1 = float(input("Operando: "))

        operador = input("Operador: ")

        operando2 = float(input("Operando: "))

        resultado = calcular(operando1, operador, operando2)

        if isinstance(resultado, str):
            print(resultado)
        else:

            print(f"{operando1} {operador} {operando2} = {resultado}")

    except ValueError:
        print("Error: Entrada no válida. Asegúrese de ingresar números reales.")

    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        
        break