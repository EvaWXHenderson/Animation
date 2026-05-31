import matplotlib.pyplot as plt
import matplotlib.colors as col

def read(image, height, width):
    grid = []

    for row in range(11, 10+height):
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

def animate(file):
    with open(file) as f:
        data = f.readlines()

    width_ = int(data[3][-3] + data[3][-2])
    height_ = int(data[4][-3] + data[4][-2])
    
    grid = read(image = data, height=height_, width=width_)
    rgb_grid = rgb(grid)

    plt.style.use('_mpl-gallery-nogrid')
    fig, ax = plt.subplots(figsize = (5,5))
    ax.imshow(rgb_grid)

    plt.xticks([]) 
    plt.yticks([])

    plt.show()

animate(file = "Piskel3.c")