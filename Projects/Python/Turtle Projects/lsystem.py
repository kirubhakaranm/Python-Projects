"""
file: lsystem.py
description: CSCI-603: Lab 2: Lindermayer system (L-System) drawing generator
language: python3
author: Kirubhakaran Meenakshi Sundaram, km1079@g.rit.edu

A program that combines a string rewriting L-system and an interpreter
to generate 2D drawings using the 2D turtle graphics library.
"""
import turtle

# Global Constants for turtle's window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
# Global Variables
states = []
distance_global = 0
angle_global = 0
output_string_global = ""
no_of_steps_global = 0
axiom_global = ""
initial_heading_global = 0
rules_global = []
COLOR_PALETTE = ["black", "red", "blue", "yellow", "brown", "cyan", "gold", "maroon", "orange", "violet"]

def get_user_input():
    """
    This function gets all the user inputs necessary for the initiating the L-System drawing generator
    :pre: None
    :post: None
    :return: None
    :param: None
    """

    global distance_global, angle_global, axiom_global, rules_global, no_of_steps_global, initial_heading_global

    print("Welcome to the L-system drawing generator!")
    axiom_global = input("Enter axiom (initial string): ")
    no_of_rules_global = int(input("Enter the number of rules: "))
    rules_global = []
    for rule_num in range(no_of_rules_global):
        rule = input("Enter rule #" + str(rule_num) + ": ")
        rule_symbol, rule_string = rule.split("=")
        rule_symbol = rule_symbol.strip()
        rule_string = rule_string.strip()
        rules_global.append([rule_symbol, rule_string])

    initial_orientation = int(input("Enter angle of rotation: "))
    initial_distance = int(input("Enter initial line segment's length: "))
    initial_heading_global = int(input("Enter initial heading: "))
    no_of_steps_global = int(input("Enter number of steps: "))

    distance_global = initial_distance
    angle_global = initial_orientation

def generate_lsystem(axiom: str, rules: list, no_of_steps: int) -> str:
    """
    This function generates the L-system based on the user given inputs
    :pre: None
    :post: None
    :return: L-system string
    :param:
            axiom: a string defining the axiom of the L-system to be drawn
            rules: a list defining the production rules of the L-system to be drawn
            no_of_steps: an integer defining the no of steps required for the L-system to be drawn
    """
    result_string = axiom[:]
    for step in range(no_of_steps-1):
        temp_string = ""
        for ch in result_string:
            temp_string += find_rule(ch, rules)
        result_string = temp_string[:]
    print("Generating the string ...")
    return result_string

def find_rule(symbol: str, rules: list) -> str:
    """
    This function returns the string corresponding to the given symbol based on the production rules
    :pre: None
    :post: None
    :return: a string that corresponds to given input symbol based on the production rules
    :param:
            symbol: a string to which the rule to be found
            rules: a list containing the all production rules
    """

    global output_string_global
    for rule in rules:
        rule_symbol = rule[0]
        if symbol == rule_symbol:
            output_string_global = rule[1]
            return output_string_global
    return symbol

def evaluate(output_string):
    """
    This function converts the L-system command in the string format to turtle drawings
    :pre: Turtle faces towards initial_heading_global
    :post: None (varies depending on the inputs)
    :return: None
    :param:
            output_string: a string the defines the L-system command
    """
    global distance_global, angle_global, COLOR_PALETTE
    init()
    print("Drawing ...")
    for pos, command in enumerate(output_string):
        palette_pos = COLOR_PALETTE.index(turtle.pencolor())
        if (command == "F") or (command == "G"):  # Moves turtle in forward direction with "pen down" condition
            turtle.pendown()
            print("forward(" + str(float(distance_global)) + ")")
            turtle.forward(distance_global)
            turtle.penup()
        elif command == "f": # Moves turtle in forward direction with "pen up" condition
            turtle.penup()
            print("pen up")
            print("forward(" + str(float(distance_global)) + ")")
            turtle.forward(distance_global)
            print("pen down")
            turtle.pendown()
        elif command == "+": # Rotate turtle towards left
            print("left(" + str(angle_global) + ")")
            turtle.left(angle_global)
        elif command == "-": # Rotates turtle towards right
            print("right(" + str(angle_global) + ")")
            turtle.right(angle_global)
        elif command == "[":  # Saving the turtle's position
            saved_pos_x, saved_pos_y = turtle.xcor(), turtle.ycor()
            saved_orientation = turtle.heading()
            saved_pen_size = turtle.pensize()
            saved_pen_color = turtle.pencolor()
            saved_length = distance_global  # (current distance)
            states.append([saved_pos_x, saved_pos_y, saved_orientation, saved_pen_size, saved_pen_color, saved_length])
            print("saving turtle's state ...")
            print(f"\t position: ({round(saved_pos_x,2)},{round(saved_pos_y,2)})")
            print(f"\t heading: {saved_orientation}")
            print(f"\t line segment's length: {round(float(saved_length),2)}")
            print(f"\t pen size: {saved_pen_size}")
            print(f"\t color: '{saved_pen_color}'")
        elif command == "]": # restoring the turtle's position
            (saved_pos_x, saved_pos_y, saved_orientation, saved_pen_size, saved_pen_color, saved_length) = states.pop()
            turtle.goto(saved_pos_x, saved_pos_y)
            turtle.setheading(saved_orientation)
            turtle.pensize(saved_pen_size)
            turtle.pencolor(saved_pen_color)
            distance_global = saved_length
            print("restoring turtle's state ...")
            print(f"\t position: ({round(saved_pos_x,2)},{round(saved_pos_y,2)})")
            print(f"\t heading: {saved_orientation}")
            print(f"\t line segment's length: {round(float(distance_global),2)}")
            print(f"\t pen size: {saved_pen_size}")
            print(f"\t color: '{saved_pen_color}'")
        elif (command == "<") or (command == ">"): # changing the pen color from the color palette
            if (output_string[pos + 1:pos + 3]).isnumeric():
                val = int(output_string[pos + 1:pos + 3])
            else:
                val = 1
            if command == "<":
                print("pencolor('" + COLOR_PALETTE[(palette_pos + val) % 10] + "')")
                turtle.pencolor(COLOR_PALETTE[(palette_pos + val) % 10])
            elif command == ">":
                print("pencolor('" + COLOR_PALETTE[palette_pos - val] + "')")
                turtle.pencolor(COLOR_PALETTE[palette_pos - val])
        elif command == "@": # changing the line segment of the turtle
            multiplier = float(output_string[pos+1:pos+4])
            distance_global *= multiplier #(Use this distance whenever moving hereafter)
        elif command == "#": # changing the pen size of the turtle
            if (output_string[pos + 1:pos + 3]).isnumeric():
                val = int(output_string[pos + 1:pos + 3])
            else:
                val = 1
            print("pensize("+ str(val) + ")")
            turtle.pensize(val)

def init():
    """
    Initialize for drawing.  (-500, -500) is in the lower left and
    (500, 500) is in the upper right.
    :pre: pos (0,0), heading (east), down
    :post: pos (0,0), heading (east), up
    :return: None
    """
    global initial_heading_global
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.setheading(initial_heading_global)
    turtle.title('L-System Generator')
    turtle.speed(6)
    #The turtle has been made deliberately visible to match the sample output images provided
    #turtle.hideturtle()

def main() -> None:
    """
    The main loop responsible for getting the input details from the user,
    printing in the standard output the resulting string generated by the L-system
    and drawing its graphical representation
    :return: None
    """
    global output_string_global, rules_global
    get_user_input()
    output_string_global = generate_lsystem(axiom_global, rules_global, no_of_steps_global)
    print("Result:")
    print(output_string_global)
    turtle.tracer(0,0)
    turtle.pendown()
    evaluate(output_string_global)
    turtle.update()
    turtle.mainloop()

if __name__ == '__main__':
    main()