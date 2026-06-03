import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as an
import matplotlib.colors as col
import functools as fct

def read(image, frame, height, width):
    grid = []

    startline = 11 + (frame*34)
    endline = (startline - 1) + height
    
    for row in range(startline, endline):
        row = image[row].split()
        for entry in range(0,width):
            row[entry] = row[entry].replace(",", "")

            red = row[entry][8:]
            green = row[entry][6:8]
            blue = row[entry][4:6]

            row[entry] = "#" + red + green + blue

        grid.append(row)

    return grid

def rgb(grid):
    rgb_grid = []
    hex_row = []

    for row in grid:
        for colour in row:
            hex_row.append(col.to_rgb(colour))
        rgb_grid.append(hex_row)
        hex_row = []

    return rgb_grid

def show_close(file):
    with open(file) as f:
        data = f.readlines()

    width_ = int(data[3][-3] + data[3][-2])
    height_ = int(data[4][-3] + data[4][-2])
    
    grid = read(image = data, frame = 0, height=height_, width=width_)
    rgb_grid = rgb(grid)

    plt.ion()

    plt.style.use('_mpl-gallery-nogrid')
    fig, ax = plt.subplots(figsize = (5,5))

    plt.xticks([]) 
    plt.yticks([])

    ax.imshow(rgb_grid)

def show(file):
    with open(file) as f:
        data = f.readlines()

    width_ = int(data[3][-3] + data[3][-2])
    height_ = int(data[4][-3] + data[4][-2])
    
    grid = read(image = data, frame = 0, height=height_, width=width_)
    rgb_grid = rgb(grid)

    plt.style.use('_mpl-gallery-nogrid')
    fig, ax = plt.subplots(figsize = (5,5))

    plt.xticks([]) 
    plt.yticks([])

    ax.imshow(rgb_grid)

def animate(file, speed):
    def grid(frame, width, height):
        grid = read(image = data, frame = frame, height=height, width=width)
        rgb_grid = rgb(grid)
        ax.imshow(rgb_grid)

    with open(file) as f:
        data = f.readlines()
    
    frames = int((len(data)-11)/33)
    width_ = int(data[3][-3] + data[3][-2]) #32
    height_ = int(data[4][-3] + data[4][-2]) #32


    plt.style.use('_mpl-gallery-nogrid')
    fig, ax = plt.subplots(figsize = (5,5))

    anim = an(fig, fct.partial(grid,width = width_,height = height_), frames = frames, interval = speed)

    plt.xticks([]) 
    plt.yticks([])
    plt.show()

def close(image, command):
    input(command)
    plt.close(image)

#image = animate(file = "Test_gif1.c", speed = 10)

#image = show("Test_image1.c")

#image = show_close("Test_image1.c"")
#close(image, "press enter to close window") #issue - now need a close() line to have plot show