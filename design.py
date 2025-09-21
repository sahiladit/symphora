import turtle
import math

# --- TURTLE SETUP ---
window = turtle.Screen()
window.bgcolor("white")
window.title("Final 10x10 Kolam")
pen = turtle.Turtle()
pen.speed(0) # Fastest speed
pen.hideturtle()
pen.width(2)
pen.color("black")

# --- DRAWING PARAMETERS (10x10 Grid) ---
GRID_SIZE = 40
ROWS = 10
COLS = 10
START_X = -GRID_SIZE * (COLS - 1) / 2
START_Y = GRID_SIZE * (ROWS - 1) / 2

# Dictionary to store (row, col) -> (x, y) mapping for easy access
dots = {} 
def draw_dots():
    pen.penup()
    for row in range(ROWS):
        for col in range(COLS):
            x = START_X + col * GRID_SIZE
            y = START_Y - row * GRID_SIZE
            dots[(row, col)] = (x, y)
            pen.goto(x, y)
            pen.dot(5, "red")

# --- CORE DRAWING LOGIC ---

def draw_symmetrical_motif(quadrant_points):
    """Draws one quadrant of the Kolam based on a list of dot coordinates."""
    
    pen.penup()
    pen.goto(dots[quadrant_points[0]])
    pen.pendown()
    
    for i in range(1, len(quadrant_points)):
        pen.goto(dots[quadrant_points[i]])

def draw_kolam_pattern():
    """Orchestrates the drawing of the entire Kolam."""
    draw_dots()
    
    # Define a set of points for one quadrant
    quadrant1 = [
        (0,0), (0,2), (2,2), (2,0), (0,0),
        (0,4), (1,3), (2,4), (3,3), (4,4),
        (4,2), (3,1), (2,2)
    ]
    
    # Draw all 4 symmetrical quadrants
    # I'll manually plot the symmetrical points to avoid errors
    # and ensure the Kolam is drawn correctly.

    # Quadrant 1 (Top-Left)
    draw_symmetrical_motif(quadrant1)

    # Quadrant 2 (Top-Right)
    quadrant2 = [(r, 9-c) for r, c in quadrant1]
    draw_symmetrical_motif(quadrant2)

    # Quadrant 3 (Bottom-Right)
    quadrant3 = [(9-r, 9-c) for r, c in quadrant1]
    draw_symmetrical_motif(quadrant3)

    # Quadrant 4 (Bottom-Left)
    quadrant4 = [(9-r, c) for r, c in quadrant1]
    draw_symmetrical_motif(quadrant4)

    # Now add the central lines that complete the design
    pen.penup()
    pen.goto(dots[(2,2)])
    pen.pendown()
    pen.goto(dots[(7,7)])

    pen.penup()
    pen.goto(dots[(2,7)])
    pen.pendown()
    pen.goto(dots[(7,2)])

# --- MAIN PROGRAM EXECUTION ---
if _name_ == "_main_":
    draw_kolam_pattern()
    turtle.done(
