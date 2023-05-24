import turtle

def draw_circle(turtle, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def flower_of_life(turtle, radius, depth):
    if depth == 0:
        return

    draw_circle(turtle, turtle.xcor(), turtle.ycor(), radius)

    for _ in range(6):
        flower_of_life(turtle, radius/3, depth-1)
        turtle.penup()
        turtle.forward(radius)
        turtle.right(60)
        turtle.pendown()

window = turtle.Screen()
window.bgcolor("white")

my_turtle = turtle.Turtle()
my_turtle.speed(0)

flower_of_life(my_turtle, 100, 4)

turtle.done()
