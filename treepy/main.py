from turtle import *


def main():
    __tree(50)


def __tree(n):
    speed(0)
    left(90)
    forward(3 * n)
    color("orange", "yellow")
    begin_fill()
    left(126)
    for i in range(5):
        forward(n / 5)
        right(144)
        forward(n / 5)
        left(72)
    end_fill()
    right(126)

    color("dark green")
    backward(n * 4.8)

    def tree(d, s):
        if d <= 0: return
        forward(s)
        tree(d - 1, s * .8)
        right(120)
        tree(d - 3, s * .5)
        right(120)
        tree(d - 3, s * .5)
        right(120)
        backward(s)

    tree(15, n)
    backward(n / 2)

    import time
    time.sleep(60)


def print_tree():
    """prints a xmas tree
    treepy.print_tree()
    """
    __tree(50)


if __name__ == '__main__':
    main()
