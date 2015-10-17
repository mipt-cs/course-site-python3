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
	space.create_text(30, 80, text = 'Solar system', font = header_font)
	return space

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

def read_sun_parameters_from_file(input_filename):
	"""считывает данные о солнце из файла.
	В данный момент читает первую строчку из файла.
	Предполагается такая строка
	1000 0 0 0 0 10 red"""
	input_file = open(input_filename)
	line = input_file.readline()
	m, x, y, Vx, Vy = [float(value) for value in line.split()[:5]]
	R = int(line.split()[5])
	color = line.split()[6]
	sun_values = PlanetValues(m, x, y, Vx, Vy, R, color)
	return sun_values

def write_planet_parameters_to_file(output_filename, sun_parameters):
	pass

def main():
	print('Modelling started!')

	root = tkinter.Tk()
	space = init_space(root)

	sun_parameters = read_sun_parameters_from_file(in_filename)
	sun = Planet(space, sun_parameters)
	
	write_planet_parameters_to_file(out_filename, sun_parameters)

	space.pack()
	root.mainloop()
	print('Modelling finished!')

if __name__ == "__main__":
	main()
