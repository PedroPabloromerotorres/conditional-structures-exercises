#Ejercicio sacado de [Camp09].

#El riesgo de que una persona sufra enfermedades coronarias depende de su edad y su índice de masa corporal:

# 	       edad < 45 edad ≥ 45
#IMC < 22.0	bajo	medio
#IMC ≥ 22.0	medio	alto
#El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.

#Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

#[Camp09]	Jennifer Campbell et al. Practical Programming: An Introduction to Computer Science Using Python. Pragmatic Bookshelf, 2009.

def calcular_imc(peso, estatura):
    """Calcula el índice de masa corporal (IMC)."""

    return peso / (estatura ** 2)

def determinar_riesgo(edad, imc):
    """Determina la condición de riesgo según la edad y el IMC."""

    if edad < 45:

        if imc < 22.0:
            return "bajo"

        else:
            return "medio"

    else:

        if imc < 22.0:
            return "medio"
            
        else:
            return "alto"

try:
    estatura = float(input("Ingrese su estatura en metros: "))

    peso = float(input("Ingrese su peso en kilos: "))

    edad = int(input("Ingrese su edad: "))

    imc = calcular_imc(peso, estatura)
    
    riesgo = determinar_riesgo(edad, imc)

    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

    print(f"Condición de riesgo: {riesgo}")

except ValueError:
    print("Por favor, ingrese valores válidos.")