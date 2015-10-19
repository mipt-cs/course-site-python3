# coding: utf-8

from solar_objects import *
from solar_vis import *


def read_space_objects_data_from_file(input_filename, space):
    """считывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов"""
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
    """считывает данные о звезде из строки.
    Предполагается такая строка:
    Star 10 red 1000 1 2 3 4
    где Star -- признак звезды, 10 - визуальный радиус в пикселах, red -- цвет
    1000 -- масса, 1 и 2 -- x и y координаты, 3 и 4 -- скорости Vx и Vy"""
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
    """считывает данные о планете из строки.
    Предполагается такая строка:
    Planet 5 green 10 1 2 3 4
    где Planet -- признак объекта-планеты, 5 - визуальный радиус в пикселах, green -- цвет
    10 -- масса, 1 и 2 -- x и y координаты, 3 и 4 -- скорости Vx и Vy"""
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
    pass


if __name__ == "__main__":
    print("This module is not for direct call!")
