# coding: utf-8

import tkinter
from solar_objects import *
from solar_vis import *
from solar_model import *
from solar_input import *

in_filename = 'solar_system.txt'
out_filename = 'result_positions.txt'

perform_execution = False

def execution():
    global physical_time
    global displayed_time
    recalculate_space_objects_positions(space_objects)
    #for body in space_objects:
    #    update_object_position(space, body)
    physical_time += dt
    displayed_time.set("%.1f"%physical_time + " seconds gone")

    if perform_execution:
        space.after(110 - int(time_speed.get()), execution)


def start_execution():
    global perform_execution
    perform_execution = True
    start_button['text'] = "Pause"
    start_button['command'] = stop_execution
    execution()
    print('Started execution...')


def stop_execution():
    global perform_execution
    perform_execution = False
    start_button['text'] = "Start"
    start_button['command'] = start_execution
    print('Paused execution.')


def main():
    global physical_time
    global displayed_time
    global time_speed
    global space
    global space_objects
    global start_button

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    header = "A long time ago in a galaxy far, far away..."
    space.create_text(30, 80, tag="header", text=header, font=header_font)
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)
    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)
    start_button = tkinter.Button(text="Start", command=start_execution)
    start_button.pack(side=tkinter.LEFT)
    """load_file_button = tkinter.Button(text="Load parameters")
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(text="Save parameters")
    save_file_button.pack(side=tkinter.LEFT)"""

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time)
    time_label.pack(side=tkinter.RIGHT)

    space_objects = read_space_objects_data_from_file(in_filename, space)

    root.mainloop()

    print('Modelling finished!')

if __name__ == "__main__":
    main()
