import turtle

#Definimos la función que creará la estrella

def pintar_estrella(picos,longitud):
    turtle.title("Dibujar estrella")
    turtle.speed(4)
     

     #Bucle para determinar las dimensiones y como se va a pintar la estrella
    for i in range(picos):
        turtle.forward(longitud)
        turtle.right(180-(180/picos))
     
     #Funcionalidad para que no se vaya el dibujo en cuanto se acabe
    turtle.exitonclick()

#Print de la estrella con los picos y longitud deseados
pintar_estrella(5,180)

