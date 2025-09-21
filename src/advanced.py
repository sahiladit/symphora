import turtle
import math

def arc_from_cell_center(t, cx, cy, r, start_angle):
    t.penup()
    t.goto(cx, cy)
    t.setheading(start_angle)
    t.forward(r)
    t.right(90)
    t.pendown()
    t.circle(r, 90)  # quarter-circle
    t.penup()

# Sikku loops for a single 2x2 cell
def pattern_sikku_cell(t, ox, oy, spacing, color="#222"):
    t.color(color)
    r = spacing / 2
    # four corners
    arc_from_cell_center(t, ox, oy, r, 0)
    arc_from_cell_center(t, ox, oy, r, 90)
    arc_from_cell_center(t, ox, oy, r, 180)
    arc_from_cell_center(t, ox, oy, r, 270)

# Draw Sikku for all 2x2 cells in 3x3 grid
def pattern_sikku_all(t, rows, cols, spacing, ox, oy, color="#222"):
    for i in range(rows-1):
        for j in range(cols-1):
            cx = ox + j*spacing + spacing/2
            cy = oy - i*spacing - spacing/2
            pattern_sikku_cell(t, cx, cy, spacing, color)



def kolam_design(dot_rows=3, dot_cols=3, spacing=60):
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
    t.speed(0)
    t.hideturtle()
    t.pensize(2)
    t.color("black")

    start_x = -(dot_cols-1) * spacing/2
    start_y =  (dot_rows-1) * spacing/2
    start_pos = t.position()
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
            if (r==0 and c==0 ):
                newangle = 270
                for _ in range(0, newangle, step):
                        t.circle(radius, step)
            elif(r==0 and c==dot_cols-1):
                newangle = 270
                t.left(270)
                t.penup()
                newz = t.pos()
                t.setx(newz[0]-30)
                t.sety(newz[1]-30)
                t.pendown()
                for _ in range(0, newangle, step):
                        t.circle(radius, step)

            elif(r==dot_rows-1 and c==0):
                newangle = 270
                t.left(-270)
                t.penup()
                newz = t.pos()
                t.setx(newz[0]-30)
                t.sety(newz[1]+30)
                t.pendown()
                for _ in range(0, newangle, step):
                        t.circle(radius, step)

            elif(r==dot_rows-1 and c==dot_cols-1):
                newangle = 270
                t.left(-180)
                t.penup()
                newz = t.pos()
                t.setx(newz[0]-60)
                t.sety(newz[1])
                t.pendown()
                for _ in range(0, newangle, step):
                        t.circle(radius, step)


            else:
                if(r==0 and c==dot_cols-2):
                    for _ in range(0, angle, step):
                        t.circle(radius, -step)
                elif(r==dot_rows-1 and c==dot_cols-2):
                     t.left(180)
                     newz = t.pos()
                     t.penup()
                     t.setx(newz[0]-60)                     
                     t.pendown()
                     for _ in range(0, angle, step):
                        t.circle(radius, -step)
                elif(r==dot_rows-2 and c==dot_cols-2):
                     t.left(-90)
                     newz = t.pos()
                     t.penup()
                     t.setx(newz[0]+30)
                     t.sety(newz[1]-30)                     
                     t.pendown()
                     for _ in range(0, angle, step):
                        t.circle(radius, -step)
                elif(r==dot_rows-2 and c==0):
                     t.left(90)
                     newz = t.pos()
                     t.penup()
                     t.setx(newz[0]-30) 
                     t.sety(newz[1]+30)                    
                     t.pendown()
                     for _ in range(0, angle, step):
                        t.circle(radius, -step)
                
                else:
                     t.color("black")
                     newz = t.pos()
                     t.penup()
                     t.setx(newz[0]-120)                     
                     t.pendown()
                     for _ in range(0, 360, step):
                        t.circle(radius, step)

                     newz = t.pos()
                     t.penup()
                     t.setx(newz[0]+60)
                     t.sety(newz[1]+60)                     
                     t.pendown()
                     for _ in range(0, 360, step):
                        t.circle(radius, step)

                     newz = t.pos()
                     t.penup()
                     t.setx(newz[0])
                     t.sety(newz[1]-120)                     
                     t.pendown()
                     for _ in range(0, 360, step):
                        t.circle(radius, step)
                    
                     newz = t.pos()
                     t.penup()
                     t.setx(newz[0]+60)
                     t.sety(newz[1]+60)                     
                     t.pendown()
                     for _ in range(0, 360, step):
                        t.circle(radius, step)
                    
                     pattern_sikku_all(t, dot_rows, dot_cols, spacing, start_x, start_y, "#222")
            
            t.penup()


    
    screen.exitonclick()

if __name__ == "__main__":
    kolam_design(dot_rows=3, dot_cols=3, spacing=60)


