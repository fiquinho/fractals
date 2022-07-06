import turtle


WIDTH, HEIGHT = 500, 500
START_X, START_Y = 0, -int(HEIGHT * 0.8 / 2)
RECURSION = 5
STARTING_LENGTH = 100


SPLIT = 4
ANGLE = 30


def setup_window():

    # Set up the window
    turtle.title("Fractal Tree")
    turtle.setup(WIDTH, HEIGHT)

    # Indicates RGB numbers will be in  the range 0 to 255
    turtle.colormode(255)
    turtle.hideturtle()

    # Batch drawing to the screen for faster rendering
    turtle.tracer(10)

    # Speed up drawing process
    turtle.speed(10)

    turtle.penup()
    turtle.goto(START_X, START_Y)
    turtle.setheading(90)


def draw_lines(length: int, depth: int, angle: int, branches: int):

    # Draw the current branch
    turtle.width(depth + 1)
    turtle.color("green" if depth <= 1 else "brown")
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()

    start_branch_angle = angle * (branches - 1) / 2
    if depth > 0:
        # Point turtle into the first branch
        turtle.left(start_branch_angle)

        for i in range(branches):
            draw_lines(int(length * 0.75), depth - 1, angle, branches)
            if i < SPLIT - 1:
                turtle.right(angle)

        turtle.left(start_branch_angle)

    turtle.left(180)
    turtle.forward(length)
    turtle.left(180)


def draw_fractal_tree(branches: int, angle: int, depth: int):
    setup_window()
    draw_lines(STARTING_LENGTH, depth, angle, branches)
    turtle.exitonclick()


def main():
    setup_window()
    draw_lines(STARTING_LENGTH, RECURSION, ANGLE, SPLIT)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
