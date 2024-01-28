import turtle


def draw_pifagoras_tree(branch_length, level):
    if level == 0:
        return
    else:
        turtle.forward(branch_length)
        turtle.left(45)
        draw_pifagoras_tree(0.6 * branch_length, level - 1)
        turtle.right(90)
        draw_pifagoras_tree(0.6 * branch_length, level - 1)
        turtle.left(45)
        turtle.backward(branch_length)


recursion_level = int(input("Введіть рівень рекурсії для фрактала дерева Піфагора: "))

turtle.speed(11)
turtle.left(90)

draw_pifagoras_tree(100, recursion_level)

turtle.exitonclick()
