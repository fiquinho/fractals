import turtle
import random

WIDTH, HEIGHT = 500, 500
START_X, START_Y = 0, -int(HEIGHT * 0.8 / 2)
STARTING_LENGTH = 100
LEAF_COLOR_PROPORTION = 0.7

RECURSION = 5
SPLIT = 4
ANGLE = 30
DRAW_CHANCE = 0.85


def setup_window():

    # Set up the window
    turtle.title("Fractal Tree")
    turtle.setup(WIDTH, HEIGHT)
    turtle.bgcolor("lightblue")

    # Indicates RGB numbers will be in  the range 0 to 255
    turtle.colormode(255)
    # turtle.hideturtle()

    # Batch drawing to the screen for faster rendering
    # turtle.tracer(20)

    # Speed up drawing process
    # turtle.speed(10)

    turtle.penup()
    turtle.goto(START_X, START_Y)
    turtle.setheading(90)


def draw_lines(length: int, depth: int, angle: int,
               branches: int, draw_chance: float):

    # Draw the current branch
    turtle.width(depth + 1)

    color_chance = random.uniform(0, 1)
    leaf_color = "green" if color_chance < LEAF_COLOR_PROPORTION else "#EEEEEE"

    turtle.color(leaf_color if depth <= 1 else "#4e342e")
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()

    start_branch_angle = angle * (branches - 1) / 2
    if depth > 0:
        # Point turtle into the first branch
        turtle.left(start_branch_angle)

        for i in range(branches):
            chance = random.uniform(0, 1)
            if chance < draw_chance:
                draw_lines(int(length * 0.75), depth - 1, angle, branches, draw_chance)
            if i < SPLIT - 1:
                turtle.right(angle)

        turtle.left(start_branch_angle)

    turtle.backward(length)


def draw_fractal_tree(branches: int, angle: int, depth: int, draw_chance: float):
    setup_window()
    draw_lines(STARTING_LENGTH, depth, angle, branches, draw_chance)
    turtle.exitonclick()


def main():
    draw_fractal_tree(SPLIT, ANGLE, RECURSION, DRAW_CHANCE)


if __name__ == '__main__':
    main()
