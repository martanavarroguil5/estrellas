import turtle

def dibujar_estrella():
    num_puntas = int(input("Ingrese el número de puntas para la estrella (debe ser al menos 5): "))
    longitud = 100
    
    '''
    si trabajamos con "estrellas" de menos de 5 puntas nos salen figuras geometricas distintas (triangulos, cuadrados, etc)'''
    if num_puntas < 5:
        print("El número de puntas debe ser al menos 5.")
        return

    angle = 180 - 180 / num_puntas #Definimos el ángulo con el que mas adelante turtle va a girar para cáda vértice de la estrella

    turtle.color("green")  #La estrella tiene color verde
    turtle.shape("turtle") #Cambiamos de forma al puntero
   
    for _ in range(num_puntas, longitud):
        turtle.forward(longitud) # Mueve la tortuga hacia adelante una distancia igual a la longitud
        turtle.right(angle) # Esto es el ángulo que gira para cada vértice

    turtle.done() #Termina de dibujar

dibujar_estrella()