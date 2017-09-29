import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(200, 200)

velocity = gr.Point(1, -2)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


while True:
    clear_window()

    draw_ball(coords)
    coords = add(coords, velocity)

    gr.time.sleep(0.02)

