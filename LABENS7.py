from PIL import Image
import math

im = Image.open("obraz .jpg")

def rysuj_kwadrat_max(obraz, m, n, k):  # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [0, 0, 0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = max(temp[0], pixel[0])
            temp[1] = max(temp[1], pixel[1])
            temp[2] = max(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

#im1 = rysuj_kwadrat_max(im,250,270,50).show()
im2 = rysuj_kwadrat_max(im, 300, 300, 170)
im2.save("obraz1.png")
#im3 = rysuj_kwadrat_max(im, 300, -300,250).show()

def rysuj_kwadrat_min(obraz, m, n, k):  # m,n - srodek kwadratu, k - długość boku kwadratu
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k / 2)
    temp = [255, 255, 255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = min(temp[0], pixel[0])
            temp[1] = min(temp[1], pixel[1])
            temp[2] = min(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

#im1 = rysuj_kwadrat_min(im,250,270,50).show()
#im2 = rysuj_kwadrat_min(im, 300, 300, 170).show()
im3 = rysuj_kwadrat_min(im, 300, -300,250)
im3.save("obraz2.png")
