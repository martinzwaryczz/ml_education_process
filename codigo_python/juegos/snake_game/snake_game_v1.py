# Vídeo para hacer el snakegame "manualmente":  https://www.youtube.com/watch?v=BP7KMlbvtOo&list=PLlEgNdBJEO-n8k9SR49AshB9j7b5Iw7hZ
# Temas con DL:
# No sé cuantas neuronas entrantaste ni intermedias tiene que haber, que lo que sí entiendo es que hay 4 de salida: arriba, abajo, izquierda, derecha
# A su vez hay 11 estados posibles a tener en cuenta: peligro arriba, peligro a la derecha, peligro a la izquierda, anda a la izquierda, anda a la derecha, anda arriba, anda abajo, comida arriba, comida abajo
#                                                     comida a la derecha, comida a la izquierda
#  

import turtle  # Librería para crear interfaces gráficas
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creamos la ventana de ejecución:
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=800, height=800)
wn.tracer(0)

# Creamos un marco indicador que terminación del juego:
border = turtle.Turtle()
border.speed(0)
border.color("black")
border.penup()
border.goto(-300, 300)
border.pendown()
border.pensize(3)

for _ in range(4):
    border.forward(600)
    border.right(90)

# Creamos la cabeza de la serpiente:
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Comida de la serpiente:
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color("red")
comida.penup()
comida.goto(0, 100)
segmentos = []

# Puntajes:
puntaje = turtle.Turtle()
puntaje.speed(0)
puntaje.shape("square")
puntaje.color("white")
puntaje.penup()
puntaje.hideturtle()
puntaje.goto(0, 320)
puntaje.write("Puntaje: 0 Mejor puntaje: 0", align="center", font=("Courier", 24, "normal"))

# Funciones de movimiento:
def go_up():
    if head.direction != "down":  # Previene el movimiento opuesto
        head.direction = "up"

def go_down():
    if head.direction != "up":  # Previene el movimiento opuesto
        head.direction = "down"

def go_left():
    if head.direction != "right":  # Previene el movimiento opuesto
        head.direction = "left"

def go_right():
    if head.direction != "left":  # Previene el movimiento opuesto
        head.direction = "right"

def move(): 
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Funciones de asignación de teclas
wn.listen()
wn.onkeypress(go_up, "w")  
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a") 
wn.onkeypress(go_right, "d")   

# Inicializamos el juego
while True:
    wn.update()

    # Estableceremos un marco de juego
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # En el mismo marco de juego, si este ya acabó, limpiamos y borramos la lista
        for segmento in segmentos:
            segmento.goto(1000, 1000)
        
        # Limpiamos la lista y el score
        segmentos.clear()
        score = 0
        puntaje.clear()
        puntaje.write(f"Puntaje {score} Mejor puntaje {high_score}", align="center", font=("Courier", 24, "normal"))

    # Si la serpiente come, que crezca, esto se hará con una lista
    if head.distance(comida) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)
        
        # Nuevo segmento
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        # delay -= 0.001

        # Incrementamos el puntaje, más adelante hacer un diccionario con top 5 puntajes:
        score +=10 

        if score > high_score:
            high_score = score
        
        puntaje.clear()
        puntaje.write(f"Puntaje {score} Mejor puntaje {high_score}", align="center", font=("Courier", 24, "normal"))

    # Movemos los nuevos segmentos con la lista: OJO CON LA IDENTACIÓN: ME QUEDE UN BUEN RATO CON DICHO PROBLEMA Y NO SABIA EL PORQUE
    for indice in range(len(segmentos) - 1, 0, -1):
         x = segmentos[indice - 1].xcor() 
         y = segmentos[indice - 1].ycor()
         segmentos[indice].goto(x, y)
              # Anda a saber 2:
    if len(segmentos) > 0:
        x = head.xcor() 
        y = head.ycor()
        segmentos[0].goto(x, y) 

    move()
    
    # Controlamos que no se choque a si misma
    for segmento in segmentos:
        if segmento.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segmento in segmentos:
                segmento.goto(1000, 1000)

            segmentos.clear()   

            score = 0
            puntaje.clear()
            puntaje.write(f"Puntaje {score} Mejor puntaje {high_score}", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
    
wn.mainloop()