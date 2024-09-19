"""
file: sunstar.py
description: CSCI-603: Lab 3: "Sun Star" generator
language: python3
author: Kirubhakaran Meenakshi Sundaram, km1079@g.rit.edu

A program that draws a Sun Star for the given inputs and an interpreter
to generate 2D drawings using the 2D turtle graphics library.
"""

import turtle
from math import cos
from math import pi

#Global constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

def init():
    """
    Initialize for drawing.  (-500, -500) is in the lower left and
    (500, 500) is in the upper right.
    :pre: pos (0,0), heading (north), down
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.setheading(90)
    turtle.title('Sun Star Generator')
    turtle.speed(6)
    turtle.pendown()
    turtle.tracer(0, 0)
    turtle.hideturtle()

def draw_side(length, level: int, angle: int) -> float:
    """
    This function draws the single side of the given Sun Star using recursion
    :pre: Turtle faces towards north
    :post: None (varies depending on the inputs)
    :return:
            side_length: an integer, which calculates the length of the entire side
    :param:
            length: an integer (float), that defines the length of the side
            level: an integer , that defines the level of the Sun Star drawing
            angle: an integer , that defines the angle of the inclination of the adjacent part
    """
    if level == 1:
        turtle.forward(length)
        return length
    else:
        side_length = 0
        side_length += draw_side(length / 4 , 1, angle)
        turtle.left(angle)
        side_length += draw_side((length / 4)/cos(angle * pi/180), level - 1, angle)
        turtle.right(2 * angle)
        side_length += draw_side((length / 4)/cos(angle * pi/180), level - 1, angle)
        turtle.left(angle)
        side_length += draw_side(length / 4, 1 , angle)
    return side_length

def draw_sun_star(sides: int, length: int, level: int, angle: int) -> float:
    """
    This function draws the entire Sun Star by repeating the draw_side() iteratively for the given number of sides
    :pre: Turtle faces towards north
    :post: None (varies depending on the inputs)
    :return:
            total_length: an integer, which calculates the total length of the entire Sun Star
    :param:
            sides: an integer (float), that defines the number of the sides of the Sun Star
            length: an integer (float), that defines the length of the side
            level: an integer , that defines the level of the Sun Star drawing
            angle: an integer , that defines the angle of the inclination of the adjacent part
    """
    total_length = 0
    for _ in range(sides):
        total_length += draw_side(length, level, angle)
        turtle.right(360/sides)
    turtle.update()
    return total_length

def main() -> None:
    """
    The main loop responsible for getting the input details from the user,
    printing in the standard output and drawing graphical representation of the Sun Star
    :return: None
    """
    # Get the user inputs
    user_inputs = [0, 0, 0, 0]
    prompts = ["Number of sides: ", "Length of initial side: ", "Number of levels: ", "Deflection angle: "]
    # Error checking and re-prompting
    for i in range(len(user_inputs)):
        user_input = ""
        if (i == 3) and (user_inputs[2] == 1):
            continue
        while True:
            try:
                user_input = input(prompts[i])
                user_inputs[i] = int(user_input)
                break
            except ValueError:
                print(f"Value must be an integer. You entered {user_input}.")

    no_of_sides, length_of_initial_side, no_of_levels, deflection_angle = user_inputs
    # Initialize the turtle window
    init()
    # Draw the sun star of the given inputs
    print("Total length is ", draw_sun_star(no_of_sides, length_of_initial_side, no_of_levels, deflection_angle))
    turtle.mainloop()

if __name__ == '__main__':
    main()