import turtle
import random

s= turtle.Screen()
s.title("Juego Tortugas")
s.bgcolor("#87A8A4")
#t= turtle.Turtle()
jugador1= turtle.Turtle()
jugador2= turtle.Turtle()


jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("white","white")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250, 225)
jugador1.showturtle()

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("black", "black")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250, -170)
jugador2.showturtle()

dado = [1,2,3,4,5,6]
for  i in range(20):
     if jugador1.pos()>=(200,200):
         print("La tortuga Blanca a Ganado")
         break
     elif jugador2.pos()>=(200,-200):
         print("La tortuga Negra a Ganado")
         break
     else:
         turno1 = input("Presione la tecla Enter para avanzar la tortuga Blanca")
         turno1= random.choice(dado)
         print ("Tu numero es: ", turno1, "\nAnvanzas:", turno1*20) # El programa  debe saber que la tortuga avanza mas de 20
         jugador1.pendown()
         jugador1.forward(20*turno1)

         turno2 = input("Presione la tecla Enter para avanzar la tortuga Negra")
         turno2= random.choice(dado)
         print ("Tu numero es: ", turno2, "\nAnvanzas:", turno2*20)
         jugador2.pendown()
         jugador2.forward(20*turno2)

turtle.done()
