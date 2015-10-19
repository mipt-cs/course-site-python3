# coding: utf-8

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты"""


header_font = "Arial-16"
window_width = 800
window_height = 600

scale_x_factor = 1
scale_y_factor = 1


def scale_x(x):
    """возвращает экранную x координату по x координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода x координаты за пределы экрана возвращает
    координату, лежащую за пределами холста."""
    return int(x*scale_x_factor) + window_width//2


def scale_y(y):
    """возвращает экранную y координату по y координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода y координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели Y смотрел вверх."""
    return int(-y*scale_y_factor) + window_height//2


def create_star_image(space, star):
    """Создаёт отображаемый объект звезды.
    Принимает физические координаты объекта."""
    x = scale_x(star.x)
    y = scale_y(star.y)
    r = star.R
    star.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def create_planet_image(space, planet):
    """Создаёт отображаемый объект планеты.
    Принимает физические координаты объекта."""
    x = scale_x(planet.x)
    y = scale_y(planet.y)
    r = planet.R
    planet.image = space.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def update_object_position(space, body):
    """Перемещает отображаемый объект планеты.
    Принимает физические координаты объекта."""
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r)  # положить за пределы окна
    space.coords(body.image, x - r, y - r, x + r, y + r)


if __name__ == "__main__":
    print("This module is not for direct call!")
