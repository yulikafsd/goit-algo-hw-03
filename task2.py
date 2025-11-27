import turtle

recur_depth = int(input("Plese choose the depth: "))

screen = turtle.Screen()
t = turtle.Turtle()
t.up()
t.setpos(-150, 100)
t.down()


def koch_side(n):
    if n == 0:
        t.forward(10)
    else:
        for angle in [60, -120, 60, 0]:
            koch_side(n - 1)
            t.left(angle)


if __name__ == "__main__":
    for _ in range(3):
        koch_side(recur_depth)
        t.right(120)
    screen.mainloop()
