import turtle


def draw_circle(x, y, size, filled=True, fill_colour='white'):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    if filled:
        turtle.fillcolor(fill_colour)
        turtle.begin_fill()

    turtle.circle(size)

    if filled:
        turtle.end_fill()


def draw_semi_circle(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(size, 180)


def draw_eye(x, y, size):
    draw_circle(x, y, size)
    draw_circle(x, y + (size / 2), (size / 2), 'black')


def draw_mouth(x, y, size):
    draw_semi_circle(x, y, size)


def draw_face():
    """ Draw a smiley face """

    # Draw outline
    draw_circle(40, 10, 100)

    # Draw left eye
    draw_eye(0, 100, 20)

    # Draw right eye
    draw_eye(80, 100, 20)

    # Draw mouth
    draw_mouth(0, 70, 40)


print('Welcome to the Smiley Face App')

print('Set up Screen')
turtle.title("Smiley Face")
turtle.setup(400, 500, 0, 0)
turtle.hideturtle()

print('Draw the face')
draw_face()

turtle.done()
print('Done')
