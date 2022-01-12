import random

from PIL import Image

pg = 0


def progressbar(pg):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[" + pg * "#" + (48 - pg) * "_" + "]" + str(int(pg / 0.48)) + "%")


progressbar(pg)
pg += 1

eyebrow = ["eyebrow_00.png", "eyebrow_01.png", "eyebrow_02.png", "eyebrow_03.png", "eyebrow_04.png", "eyebrow_05.png",
           "eyebrow_06.png", "eyebrow_07.png", "eyebrow_08.png", "eyebrow_09.png"]
eyebrow_sulyok = (10, 10, 10, 10, 10, 10, 10, 10, 10, 10)

hairs = ["hair_00.png", ""]
hairs_sulyok = (100, 0)

beards = ["beard_00.png", ""]
beards_sulyok = (100, 0)

eyes = ["eye_00.png", ""]
eyes_sulyok = (100, 0)

hats = ["hat_00.png", ""]
hats_sulyok = (100, 0)

shirts = ["shirt_00.png", ""]
shirts_sulyok = (100, 0)

teeths = ["teeth_00.png", ""]
teeths_sulyok = (100, 0)

r_ears = ["r_ear_00.png", ""]
r_ears_sulyok = (100, 0)

l_ears = ["l_ear_00.png", ""]
l_ears_sulyok = (100, 0)


def merge(background, paste):
    for ii in range(x):
        for jj in range(y):
            if paste[ii, jj][3] != 0:
                background[ii, jj] = paste[ii, jj]


N = 16
x, y = Image.open("base.png").size

for n in range(N):
    image = Image.open("base.png")
    img = image.load()
    osszeskieg = [random.choices(l_ears, l_ears_sulyok, k=1)[0], random.choices(eyebrow, eyebrow_sulyok, k=1)[0],
                  random.choices(hairs, hairs_sulyok, k=1)[0],  random.choices(hats, hats_sulyok, k=1)[0],
                  random.choices(beards, beards_sulyok, k=1)[0], random.choices(eyes, eyes_sulyok, k=1)[0],
                  random.choices(shirts, shirts_sulyok, k=1)[0],
                  random.choices(teeths, teeths_sulyok, k=1)[0], random.choices(r_ears, r_ears_sulyok, k=1)[0]]

    for kieg in osszeskieg:
        if kieg != "semmi":
            kieg = Image.open(kieg)
            ke = kieg.load()
            merge(img, ke)
    image.save(f"odgy{n}.png")
    progressbar(pg)
    pg += 1

for n in range(N):
    image = Image.open(f"odgy{n}.png")
    img = image.load()
    colors = []
    for i in range(x):
        for j in range(y):
            if img[i, j] not in colors:
                colors.append(img[i, j])

    newcolors = []
    for c in range(len(colors)):
        newcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
        newcolors.append(newcolor)

    newimage = Image.new(mode="RGBA", size=(x, y))
    newimg = newimage.load()
    for i in range(x):
        for j in range(y):
            if img[i, j] != (0, 0, 0, 255):
                newimg[i, j] = newcolors[colors.index(img[i, j])]
            else:
                newimg[i, j] = (0, 0, 0, 255)
    newimage.save(f"odgy{n}.png")
    progressbar(pg)
    pg += 1

kiegek = {"addon_00.png": 50}

for n in range(N):
    image = Image.open(f"odgy{n}.png")
    img = image.load()

    osszeskieg = []

    for kieg in kiegek:
        if random.randint(0, 100) <= kiegek[kieg]:
            osszeskieg.append(kieg)

    for kieg in osszeskieg:
        if kieg != "semmi":
            kieg = Image.open(kieg)
            ke = kieg.load()
            merge(img, ke)

    image.save(f"odgy{n}.png")
    progressbar(pg)
    pg += 1
