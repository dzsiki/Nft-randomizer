from PIL import Image
image = Image.open("base.png")
img = image.load()

x, y = Image.open("base.png").size

for i in range(x):
    for j in range(y):
        if img[i, j][3] == 0:
            img[i, j] = (0,0,0,0)

image.save("base.png")