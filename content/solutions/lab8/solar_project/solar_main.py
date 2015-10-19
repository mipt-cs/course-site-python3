import tkinter
import solar_vis as vis
import solar_model as model
import solar_input

in_filename = 'solar_system.txt'
out_filename = 'result_positions.txt'
header_font = "Arial-16"
window_width = 800
window_height = 600

scale_x_factor = 1
scale_y_factor = 1

def scale_x(x):
	"""возвращает экранную x координату по x координате модели
	принимает вещественное число, возвращает целое число
	В случае выхода x координаты за пределы экрана возвращает
	координату, лежащую за пределами холста"""
	return x*scale_x_factor + window_width//2

def scale_y(y):
	"""возвращает экранную y координату по y координате модели
	принимает вещественное число, возвращает целое число.
	Направление оси развёрнуто, чтобы у модели Y смотрел вверх.
	В случае выхода y координаты за пределы экрана возвращает
	координату, лежащую за пределами холста"""
	return -y*scale_y_factor + window_height//2

def init_space(root):
	space = tkinter.Canvas(root, width = window_width, height = window_height, bg = "black")
	space.create_text(30, 80, text = 'Солнечная система', font = header_font)
	return space

class SunValues:
	def __init__(self, m, x, y, Vx, Vy, R = 5, color = 'gray'):
		"""класс, описывающий массу, координаты, скорость планеты в метрах в секунду,
		а также визуальный радиус планеты в пикселах и её цвет"""
		self._m = m
		self._x = x
		self._y = y
		self._Vx = Vx
		self._Vy = Vy
		self._R = R
		self._color = color

class Sun():
	"""тип данных, описывающий неподвижную звезду, вокруг которой
	вращаются планеты"""
	def __init__(self, space, values):
		self._m, self._x, self._y = values._m, values._x, values._y
		self._R, self._color = values._R, values._color
		x, y = scale_x(self._x), scale_y(self._y)
		R, color = self._R, self._color
		self._avatar = space.create_oval([x - R, y - R], [x + R, y + R], fill = color)

class PlanetValues:
	def __init__(self, m, x, y, Vx, Vy, R = 5, color = 'gray'):
		"""класс, описывающий массу, координаты, скорость планеты в метрах в секунду,
		а также визуальный радиус планеты в пикселах и её цвет"""
		self._m = m
		self._x = x
		self._y = y
		self._Vx = Vx
		self._Vy = Vy
		self._R = R
		self._color = color

class Planet():
	"""тип данных, описывающий планету"""
	def __init__(self, space, values):
		self._m, self._x, self._y, self._Vx, self._Vy = values._m, values._x, values._y, values._Vx, values._Vy
		self._R, self._color = values._R, values._color
		x, y = scale_x(self._x), scale_y(self._y)
		R, color = self._R, self._color
		self._avatar = space.create_oval([x - R, y - R], [x + R, y + R], fill = color)

def read_nebular_objects_data_from_file(input_filename):
	input_file = open(input_filename)
	sun_parameters = read_sun_parameters_from_file(input_file)
	planets_parameters = []
	while not input_file.eof():
		planet_parameters = read_planet_parameters_from_file(input_file)
		planets_parameters.append(planet_parameters)
	return (sun_parameters, planets_parameters)

def read_sun_parameters_from_file(input_file):
	"""считывает данные о планете из файла.
	читает одну строчку из файла.
	Предполагается такая строка:
	Солнце 10 red 1000 0 0"""
	line = input_file.readline()
	tokens = line.split()
	name = tokens[0]
	R = int(tokens[1])
	color = tokens[2]
	m, x, y = [float(value) for value in tokens[3:6]
	sun_values = SunValues(m, x, y, name, R, color)
	return sun_values

def read_planet_parameters_from_file(input_file):
	"""считывает данные о планете из файла.
	читает одну строчку из файла.
	Предполагается такая строка
	Земля 5 green 1000 0 1000 1000 0"""
	line = input_file.readline()
	tokens = line.split()
	name = tokens[0]
	R = int(line.split()[5])
	color = line.split()[6]
	m, x, y, Vx, Vy = [float(value) for value in tokens[:5]]
	planet_values = PlanetValues(m, x, y, Vx, Vy, R, color)
	return planet_values

def write_nebular_objects_data_to_file(output_filename, sun_parameters):
	pass

def main():
	print('Modelling started!')

	root = tkinter.Tk()
	space = init_space(root)

	sun_parameters, planets_parameters = read_sun_parameters_from_file(in_filename)
	sun = Sun(space, sun_parameters)
	planets = [Planet(space, planet_parameters) for planet_parameters in planets_data]
	
	write_planet_parameters_to_file(out_filename, sun_parameters)

	space.pack()
	root.mainloop()
	print('Modelling finished!')

if __name__ == "__main__":
	main()
