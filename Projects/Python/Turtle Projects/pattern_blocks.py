"""
file: pattern_blocks.py
description: CSCI-603: Week 1 - Lab: Pattern Block
language: python3
author: Kirubhakaran Meenakshi Sundaram, km1079@g.rit.edu

This is a demo program that draws the pattern block.
"""

import turtle
from math import sqrt

# global constants for window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# global constant for the side of the shape to be drawn
side = 30

def init() -> None:
    """
    Initialize for drawing.  (-300, -300) is in the lower left and
    (300, 300) is in the upper right.
    :pre: turtle's default pos (0,0): center of canvas, heading (east), down
    :post: turtle's default pos (0,0): center of canvas, heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.pencolor("black")
    turtle.up()
    turtle.setheading(0)
    turtle.title('Pattern Block')
    turtle.speed(6)
    turtle.hideturtle()

# The above part of the program was extracted from the CSCI 603 course material (Intro Lab)
def draw_triangle(side) -> None:
    """
    This function draws a green-coloured equilateral triangle with length of given side.
    The triangle is create from its base along counter clock-wise direction
    :pre: Turtle faces towards east along the base of the triangle
    :post: Turtle faces towards east along the base of the triangle
    :return: None
    :param: 
            side: an integer input defines the length of the triangle
    """
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)

    turtle.end_fill()
    turtle.penup()    

def draw_rhombus(side, clockwise=True) -> None:
    """
    This function draws a blue-coloured equilateral rhombus with length of given side.
    Clock-wise Rhombus: Turtle starts from the top of the side of rhombus in a clock-wise direction
    Counterclock-wise Rhombus: Turtle starts from the base of the rhombus in a counter clock-wise direction
    
    :pre: Turtle faces towards east
    :post: Turtle faces towards east
    :return: None
    :param: 
            side: an integer input defines the length of the rhombus
            clockwise: a boolean value either True or False 
            (True: draws a rhombus in a clock-wise direction, False: draws a rhombus in a counter clock-wise direction)
    
    """
    
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()

    if clockwise:
        for i in range(2):
            turtle.forward(side)
            turtle.right(60)
            turtle.forward(side)
            turtle.right(120)
    else:
        for i in range(2):
            turtle.forward(side)
            turtle.left(120)
            turtle.forward(side)
            turtle.left(60)

    turtle.end_fill()
    turtle.penup()

def draw_trapezoid(side, clockwise=True) -> None:
    """
    This function draws a red-coloured isoceles trapezoid with length of given side.
    Clock-wise trapezoid: Turtle starts from the top of the side of trapezoid in a clock-wise direction
    Counterclock-wise trapezoid: Turtle starts from the base of the trapezoid in a counter clock-wise direction
    
    :pre: Turtle faces towards east
    :post: Turtle faces towards east
    :return: None
    :param: 
            side: an integer input defines the length of the trapezoid
            clockwise: a boolean value either True or False 
            (True: draws a trapezoid in a clock-wise direction, False: draws a trapezoid in a counter clock-wise direction)
    """

    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()

    if clockwise:
        turtle.forward(2 * side)
        turtle.right(120)
        turtle.forward(side)
        turtle.right(60)
        turtle.forward(side)
        turtle.right(60)
        turtle.forward(side)
        turtle.right(120)

    else:
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(2 * side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)

    turtle.end_fill()
    turtle.penup()

def draw_hexagon(side,clockwise=True,fill_color="yellow") -> None:
    """
    This function draws a yellow-coloured isoceles Hexagon with length of given side.
    Clock-wise trapezoid: Turtle starts from the top of the side of Hexagon in a clock-wise direction
    Counterclock-wise trapezoid: Turtle starts from the base of the Hexagon in a counter clock-wise direction
    
    :pre: Turtle faces towards east
    :post: Turtle faces towards east
    :return: None
    :param: 
            side: an integer input defines the length of the Hexagon
            clockwise: a boolean value either True or False 
            (True: draws a Hexagon in a clock-wise direction, False: draws a Hexagon in a counter clock-wise direction)
    """

    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    if clockwise:
        for i in range(6):
            turtle.forward(side)
            turtle.right(60)
    else:
        for i in range(6):
            turtle.forward(side)
            turtle.left(60)

    turtle.end_fill()
    turtle.penup()  

def draw_square(side, clockwise=True) -> None:
    """
    This function draws a yellow-coloured Square with length of given side.
    Clock-wise trapezoid: Turtle starts from the top of the side of Square in a clock-wise direction
    Counterclock-wise trapezoid: Turtle starts from the base of the Square in a counter clock-wise direction
    
    :pre: Turtle faces towards east
    :post: Turtle faces towards east
    :return: None
    :param: 
            side: an integer input defines the length of the Square
            clockwise: a boolean value either True or False 
            (True: draws a Square in a clock-wise direction, False: draws a Square in a counter clock-wise direction)
    """

    turtle.pendown()
    turtle.fillcolor("orange")
    turtle.begin_fill()
    
    if clockwise:
        for i in range(4):
            turtle.forward(side)
            turtle.right(90)
    else:
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

    turtle.end_fill()
    turtle.penup()  

def draw_thin_rhombus(side, clockwise=True) -> None:
    """
    This function draws a brown-coloured thin beige rhombi with a convex angle of 30 degrees with length of given side.
    Clock-wise thin rhombus: Turtle starts from the top of the side of thin rhombus in a clock-wise direction
    Counterclock-wise thin rhombus: Turtle starts from the base of the thin rhombus in a counter clock-wise direction
    
    :pre: Turtle faces towards east
    :post: Turtle faces towards east
    :return: None
    :param: 
            side: an integer input defines the length of the thin rhombus
            clockwise: a boolean value either True or False 
            (True: draws a thin rhombus in a clock-wise direction, False: draws a thin rhombus in a counter clock-wise direction)
    """  
    turtle.pendown()
    turtle.fillcolor("brown")
    turtle.begin_fill()

    if clockwise:
        for i in range(2):
            turtle.forward(side)
            turtle.right(150)
            turtle.forward(side)
            turtle.right(30)
    else:
        for i in range(2):
            turtle.forward(side)
            turtle.left(30)
            turtle.forward(side)
            turtle.left(150)

    turtle.end_fill()
    turtle.penup()  

def draw_first_base_pattern() -> None:
    """
        This pattern consists of the following:
            one blue-coloured rhombus, 
            two red-coloured isoceles trapezoid, 
            two yellow-coloured hexagon and 
            two green-coloured triangles

        #pre: Turtle faces towards east
        #post: Turtle faces towards east
        #return: None
    """

    draw_rhombus(side)
    turtle.forward(side)
    draw_trapezoid(side)
    turtle.forward(2 * side)
    draw_hexagon(side)
    # Move the turtle to the base of the hexagon pointing towards east
    turtle.right(90)
    turtle.forward(sqrt(3) * side)
    turtle.left(90)
    turtle.forward(side)
    draw_triangle(side)
    # Move the turtle to draw second trapezoid of the pattern
    turtle.backward(2 * side)
    turtle.left(120)
    draw_trapezoid(side,clockwise=False)
    turtle.right(120)
    draw_hexagon(side)
    turtle.right(90)
    turtle.forward(sqrt(3) * side)
    turtle.left(90)
    turtle.forward(side)
    draw_triangle(side)

    # Move the turtle back to origin (0, 0)
    turtle.backward(side)
    turtle.left(120)
    turtle.forward(4 * side)
    turtle.right(120)

def draw_second_base_pattern() -> None:
    """
        This pattern consists of the following:
            one brown-coloured thin rhombus
            two blue-coloured rhombus, 
            two red-coloured isoceles trapezoid, 
            one yellow-coloured hexagon and 
            two green-coloured triangles

        #pre: Turtle faces towards east
        #post: Turtle faces towards east
        #return: None
    """
    # The turtle draws the brown-coloured thin rhombus
    turtle.left(15)
    turtle.forward(side)
    turtle.right(30)
    draw_thin_rhombus(side)
    
    # The turtle draws two blue-coloured rhombi
    turtle.left(60)
    draw_rhombus(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(150)
    draw_rhombus(side, clockwise=False)

    # The turtle draws one orange-coloured square
    turtle.left(120)
    draw_square(side, clockwise=False)

    # The turtle draws two orange-coloured triangles
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.right(180)
    draw_triangle(side)   

    turtle.right(90)
    turtle.forward(side)
    turtle.right(180)
    draw_triangle(side) 

    # The turtle draws one yellow-coloured hexagon
    turtle.forward(side)
    turtle.left(105)
    draw_hexagon(side)

    # The turtle draws two red-coloured trapezoids
    turtle.forward(side)
    turtle.right(60)
    draw_trapezoid(side, clockwise=False)

    turtle.right(90)
    turtle.forward(sqrt(3) * side)
    turtle.right(90)
    turtle.backward(side)
    draw_trapezoid(side, clockwise=False)

    #The turtle moves back to the origin (0,0)
    turtle.right(90)
    turtle.forward(sqrt(3) * side // 2)
    turtle.right(90)
    turtle.backward((sqrt(3) + sqrt(2) + 0.5 + 1) * side)

def draw_first_pattern_block() -> None:
    """
        This function repeats the draw_first_base_pattern() six times with a rotation of 60 degree clock-wise direction every time.

        #pre: Turtle faces towards east
        #post: Turtle faces towards east
        #return: None
    """
    turtle.tracer(0,0)
    for no_of_patterns in range(6):
        draw_first_base_pattern()
        # Rotate the turtle to 60 degrees
        turtle.right(60)
    turtle.update()

def draw_second_pattern_block() -> None:
    """
        This function repeats the draw_second_base_pattern() five times with a rotation of 72 degree clock-wise direction every time.

        #pre: Turtle faces towards east
        #post: Turtle faces towards east
        #return: None
    """
    turtle.tracer(0,0)
    for no_of_patterns in range(5):
        draw_second_base_pattern()
        # Rotate the turtle to 72 degrees
        turtle.right(72)
    turtle.update()

def main():
    """
        The main function.
        :pre: (relative) pos (0,0), heading (east), pen down
        :post: (relative) pos (0,0), heading (east), pen up
        :return: None
    """
    init()
    
    draw_first_pattern_block()

    pause = input('Press "Enter" key to display the second pattern block...')
    
    turtle.reset()

    turtle.hideturtle()
    draw_second_pattern_block()
    turtle.mainloop()

    #print("program executed")

if __name__ == '__main__':
    main()