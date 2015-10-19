# coding: utf-8

from solar_objects import Star, Planet
# Чисто логически модуль input НЕ должен импортировать vis
from solar_vis import create_star_image, create_planet_image


def read_space_objects_data_from_file(input_filename, space):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    **space** — холст для рисования
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if line[0] == '#':
                continue  # строки, начина
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                create_star_image(space, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                create_planet_image(space, planet)
                objects.append(planet)
            elif object_type == "system_name":
                pass  # not a space object at all
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    tokens = line.split()
    assert(tokens[0].lower() == 'star')
    assert(len(tokens) == 8)
    star.R = int(tokens[1])
    star.color = tokens[2]
    star.m = float(tokens[3])
    star.x = float(tokens[4])
    star.y = float(tokens[5])
    star.Vx = float(tokens[6])
    star.Vy = float(tokens[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    tokens = line.split()
    assert(tokens[0].lower() == 'planet')
    assert(len(tokens) == 8)
    planet.R = int(tokens[1])
    planet.color = tokens[2]
    planet.m = float(tokens[3])
    planet.x = float(tokens[4])
    planet.y = float(tokens[5])
    planet.Vx = float(tokens[6])
    planet.Vy = float(tokens[7])


def write_space_objects_data_to_file(output_filename, sun_parameters):
    """FIXME Дописать. sun_parameters -> ? """
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
