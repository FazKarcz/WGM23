from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

im = Image.open("zeby.png")
obraz = im.convert('L')
obraz.show()

def konwertuj1(obraz, w_r, w_g, w_b):
    obraz = np.array(obraz)
    szerokosc, wysokosc = obraz.shape[:2]
    obraz_wynikowy = np.empty_like(obraz)
    for i in range(szerokosc):
        for j in range(wysokosc):
            R, G, B = obraz[i, j]
            L = round(R * w_r + G * w_g + B * w_b)
            obraz_wynikowy[i, j] = [L, L, L]

    return Image.fromarray(obraz_wynikowy.astype('uint8'))

im2 = im.copy()
konw = konwertuj1(im2,(299/1000),(587/1000),(114/1000))
konw.show()
