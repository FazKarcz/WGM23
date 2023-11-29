from PIL import Image
import math

obraz = Image.open('obraz.jpg')


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


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def rysuj_kolo(obraz, m_s, n_s, r, x, y):
    obraz1 = obraz.copy()
    w, h = obraz.size
    temp1 = obraz1.load()
    temp2 = obraz1.copy().load()
    for i, j in zakres(w, h):
        if (i - m_s) ** 2 + (j - n_s) ** 2 < r ** 2:  # wzór na koło o środku (m_s, n_s) i promieniu r
            x_temp = (i - m_s) + x
            y_temp = (j - n_s) + y
            temp1[i, j] = temp2[x_temp, y_temp]
    return obraz1


im = obraz.copy()
w, h = im.size
im1 = rysuj_kwadrat_max(im, 200, 170, 101)
im2 = rysuj_kwadrat_max(im1, int(w / 2), int(h / 2) - 50, 45)
im3 = rysuj_kwadrat_max(im2, 500, 850, 67)

im3.save("obraz1.png")

im_ = obraz.copy()
im_1 = rysuj_kwadrat_min(im_, int(w / 2) + 200, int(h / 2) - 200, 101)
im_2 = rysuj_kwadrat_min(im_1, int(w / 2), int(h / 2) - 50, 45)
im_3 = rysuj_kwadrat_min(im_2, 500, 850, 67)

im_3.save("obraz2.png")

im4 = obraz.copy()

im5 = rysuj_kolo(im4, int(w / 2), int(h / 2) - 50, 30, 100, 100)
im5.show()
