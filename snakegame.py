import turtle
import time
import random

# Definicija pomembnih spremenljivk
tocke = 0
najvisje_tocke = 0
zamik = 0.1 # Začetna hitrost kače
deli_telesa = []

# Pripravi zaslon
zaslon = turtle.Screen()
zaslon.title("Snake Game")
zaslon.bgcolor("green")
zaslon.setup(width=600, height=600)
zaslon.tracer(0)

# Kačja glava
glava = turtle.Turtle()
glava.speed(0)
glava.shape("square")
glava.color("black")
glava.penup()
glava.goto(100, 100)
glava.direction = "stop"

# Hrana
hrana = turtle.Turtle()
hrana.speed(0)
hrana.shape("circle")
hrana.color("red")
hrana.penup()
hrana.goto(200,200)

# Prikaz točk
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Točke: 0  Rekord: 0", align="center", font=("Courier", 24, "normal"))

# Funkcije za premikanje kače
def pojdi_gor():
    glava.direction = "up"

def premik():
    if glava.direction == "up":
        y = glava.ycor()
        glava.sety(y + 20)
    if glava.direction == "down":
        y = glava.ycor()
        glava.sety(y - 20)
    if glava.direction == "left":
        x = glava.xcor()
        glava.setx(x - 20)
    if glava.direction == "right":
        x = glava.xcor()
        glava.setx(x + 20)

# Tipke za premikanje kače
zaslon.listen()
zaslon.onkeypress(pojdi_gor, "w")

# Zanka za glavni del igre
while True:
    zaslon.update()

    # Trčenje v meje zaslona
    if glava.xcor()>290 or glava.xcor()<-290 or glava.ycor()>290 or glava.ycor()<-290:
        time.sleep(1)
        # Mesto glave po trčenju
        glava.goto(100,100)
        glava.direction = "stop"
        # Mesto hrane po trčenju
        hrana.goto(200, 200)

        # Skrij dele telesa
        for delcek in deli_telesa:
            delcek.goto(1000, 1000)
        
        # Počisti seznam deli_telesa
        deli_telesa.clear()

        # Resetiraj točke
        tocke = 0

        # Resetiraj zamik
        zamik = 0.1

        pen.clear()
        pen.write("Točke: {}  Rekord: {}".format(tocke, najvisje_tocke), align="center", font=("Courier", 24, "normal")) 


    # Trčenje v hrano
    if glava.distance(hrana) < 20:
        # Nova hrana na na x, y
        x = (-290, 290)
        y = (-290, 290)
        hrana.goto(x,y)

        # Dodaj delček telesa
        nov_delcek = turtle.Turtle()
        nov_delcek.speed(0)
        nov_delcek.shape("square")
        nov_delcek.color("grey")
        nov_delcek.penup()
        deli_telesa.append(nov_delcek)

        # Skrajšaj zamik
        zamik -= 0.001

        # Povečaj točke
        tocke += 10

        if tocke > najvisje_tocke:
            najvisje_tocke = tocke
        
        pen.clear()
        pen.write("Točke: {}  Rekord: {}".format(tocke, najvisje_tocke), align="center", font=("Courier", 24, "normal")) 

    # Premik delčkov telesa
    for index in range(len(deli_telesa)-1, 0, -1):
        x = deli_telesa[index-1].xcor()
        y = deli_telesa[index-1].ycor()
        deli_telesa[index].goto(x, y)

    # Premik delčka 0 na mesto glave
    if len(deli_telesa) > 0:
        x = glava.xcor()
        y = glava.ycor()
        deli_telesa[0].goto(x,y)

    premik()    

    # Trčenje glave v delcke telesa
    for delcek in deli_telesa:
        if delcek.distance(glava) < 20:
            time.sleep(1)
            # Premik glave po trčenju
            glava.goto(200,100)
            glava.direction = "stop"
        
            # Skrij dele telesa
            for delcek in deli_telesa:
                delcek.goto(1000, 1000)
        
            # Počisti seznam deli_telesa
            deli_telesa.clear()

            # Resetiraj točke
            tocke = 0

            # Resetiraj zamik
            zamik = 0.1
        
            # Posodobi prikaz točk
            pen.clear()
            pen.write("Točke: {}  Rekord: {}".format(tocke, najvisje_tocke), align="center", font=("Courier", 24, "normal"))

    time.sleep(zamik)

zaslon.mainloop()