#El joven periodista Solarrabietas debe relatar un partido de tenis, pero no conoce las reglas del deporte. 
# En particular, no ha logrado aprender cómo saber si un set ya terminó, y quién lo ganó.

#Un partido de tenis se divide en sets. Para ganar un set, un jugador debe ganar 6 juegos, pero además debe haber ganado por lo menos dos juegos más que su rival. 
# Si el set está empatado a 5 juegos, el ganador es el primero que llegue a 7. Si el set está empatado a 6 juegos, el set se define en un último juego, 
# en cuyo caso el resultado final es 7-6.

#Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

#si A ganó el set, o
#si B ganó el set, o
#si el set todavía no termina, o
#si el resultado es inválido (por ejemplo, 8-6 o 7-3).
#Desarrolle un programa que solucione el problema de Solarrabietas:

#Juegos ganados por A: 4
#Juegos ganados por B: 5
#Aun no termina
#Juegos ganados por A: 5
#Juegos ganados por B: 7
#Gano B
#Juegos ganados por A: 5
#Juegos ganados por B: 6
#Aun no termina
#Juegos ganados por A: 3
#Juegos ganados por B: 7
#Invalido
#Juegos ganados por A: 6
#Juegos ganados por B: 4
#Gano A

def estado_set(juegos_a, juegos_b):

    if juegos_a > 7 or juegos_b > 7 or (juegos_a == 6 and juegos_b > 6) or (juegos_b == 6 and juegos_a > 6):
        return "Inválido"
    
    if juegos_a >= 6 and juegos_a >= juegos_b + 2:
        return "Ganó A"

    elif juegos_b >= 6 and juegos_b >= juegos_a + 2:
        return "Ganó B"
    
    return "Aun no termina"

while True:

    try:
        juegos_a = int(input("Juegos ganados por A: "))

        juegos_b = int(input("Juegos ganados por B: "))
        
        resultado = estado_set(juegos_a, juegos_b)
        print(resultado)
        
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
    
    continuar = input("¿Desea ingresar otro resultado? (s/n): ")
    if continuar.lower() != 's':
        
        break