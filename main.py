from turtle import*

bgcolor("black")
pensize(2)
speed(0)

for i in range(6):
    for colors in ["red","white","cyan","green","blue","yellow","magenta"]:
        color(colors)
        circle(100)
        left(10)
        
hideturtle()
