import turtle
import math



def kolam_design(dot_rows=4, dot_cols=4, spacing=60):
    """
    Draws a simple Kolam pattern:
    - Places a dot grid (dot_rows x dot_cols)
    - Draws smooth looping curves weaving around the dots
    """
    screen = turtle.Screen()
    screen.title("Kolam Design")
    screen.bgcolor("white")
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0.5)
    t.hideturtle()
    t.pensize(2)
    t.color("black")

    start_x = -(dot_cols-1) * spacing/2
    start_y =  (dot_rows-1) * spacing/2

    t.penup()
    for r in range(dot_rows):
        for c in range(dot_cols):
            x = start_x + c*spacing
            y = start_y - r*spacing
            t.goto(x, y-3)  
            t.dot(6, "black")
    t.penup()

    radius = spacing/2
    flag = -1
    for r in range(dot_rows):
        for c in range(dot_cols):
            cx = start_x + c*spacing
            cy = start_y - r*spacing

            t.goto(cx + radius, cy)
            t.setheading(90)
            t.pendown()

            angle = 180
            step  = 10      

            if flag == 1:
                for _ in range(0, angle, step):
                    t.circle(radius, -step)
            else:
                for _ in range(0, angle, step):
                    t.circle(radius,  step)

            flag *= -1
            t.penup()


    flag = 1
    for r in range(dot_rows):
        for c in range(dot_cols):
            cx = start_x + c*spacing
            cy = start_y - r*spacing

            t.goto(cx + radius, cy)
            t.setheading(90)
            t.pendown()
            angle = 180
            step  = 10      

            if flag == 1:
                for _ in range(0, angle, step):
                    t.circle(radius, -step)
            else:
                for _ in range(0, angle, step):
                    t.circle(radius,  step)

            flag *= -1
            t.penup()
    
    screen.exitonclick()

if __name__ == "__main__":
    kolam_design(dot_rows=4, dot_cols=4, spacing=60)
