import random

from PIL import Image

x, y = 1000, 1000


asd= 0

newimage = Image.new(mode="RGBA", size=(x, y))
newimg = newimage.load()


def valami(xx, yy):
    for i in range(xx,x):
        for j in range(yy,y):

                if i % 250 == 0 and j % 250 == 0:
                    valami(i+1, j+1)

                if 100 >= (i-500+xx)**2 + (j-500+yy)**2 -250**2 >= 5000:
                    newimg[i, j] = (0, 0, 255, 255)
                else:
                    newimg[i, j] = (255, 0, 0, 255)
valami(0,0)
newimage.save(f"random.png")

"""
image = Image.open("base.png")
img = image.load()

x, y = Image.open("base.png").size

for i in range(x):
    for j in range(y):
        if img[i, j][3] == 0:
            img[i, j] = (0,0,0,0)

image.save("base.png")
"""
