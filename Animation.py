import matplotlib.pyplot as plt
import matplotlib.colors as col
import re

with open("Piskel1.c") as f:
    data = f.readlines()
    # data = list strings with each string being the corresponding line of the file

#Colours in RBGA

#Width = line 4 - 32 characters + width
width = int(data[3][-3] + data[3][-2])
#Height = line 5 - 33 characters + height
height = int(data[4][-3] + data[4][-2])

def read(file):
    grid = []

    for row in range(11, 10+height):
        row = file[row].split() #row = [list of items separated by commas in a given row]
        for entry in range(0,width):
            row[entry] = row[entry].replace(",", "") #gives wanted colour in format [ff bb gg rr] want [rr gg bb]

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

def animate(image):
    grid = read(file = image)
    print(grid)
    rgb_grid = rgb(grid)
    #rgb_grid[0][0] = (1,0,0)
    #rgb_grid[0][1] = (0,1,0)
    #rgb_grid[1][0] = (0,0,1)
    #rgb_grid[1][1] = (0,0,0)
    #print(rgb_grid)

    plt.style.use('_mpl-gallery-nogrid')
    fig, ax = plt.subplots(figsize = (5,5))
    ax.imshow(rgb_grid)
    plt.show()

animate(image = data)