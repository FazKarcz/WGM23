from PIL import Image
import numpy as np

#zadanie 1
obraz = Image.open('./lab6/obraz.jpg')
inicjaly = Image.open('./lab6/inicjaly.bmp')

#zadanie 2
def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                obraz1.putpixel((i + m, j + n), kolor)
    return obraz1
w, h = obraz.size
obraz2 = wstaw_inicjaly(obraz,inicjaly,w- 100, h - 100,100)
#obraz2.show()

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return obraz1

obraz3 = wstaw_inicjaly_maska(obraz,inicjaly,w//2,h//2,100,100,100)
#obraz3.show()

#zadanie 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    pixels_obraz1 = obraz1.load()
    pixels_inicjaly = inicjaly.load()

    for i in range(w0):
        for j in range(h0):
            if i + m < w and j + n < h:
                if pixels_inicjaly[i, j] == 0:
                    pixels_obraz1[i + m, j + n] = kolor
    return obraz1


def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    pixels_obraz1 = obraz1.load()
    pixels_inicjaly = inicjaly.load()

    for i in range(w0):
        for j in range(h0):
            if i + m < w and j + n < h:
                if pixels_inicjaly[i, j] == 0:
                    p = pixels_obraz1[i + m, j + n]
                    pixels_obraz1[i + m, j + n] = (p[0] + x, p[1] + y, p[2] + z)
    return obraz1

obraz4 = wstaw_inicjaly_load(obraz,inicjaly,100,100,100)
#obraz4.show()
obraz5 = wstaw_inicjaly_maska(obraz,inicjaly,100,100,100,100,100)
#obraz5.show()

#zadanie 4
def kontrast(obraz, wsp_kontrastu):
    obraz_kontrastowy = obraz.copy()
    pixels = obraz_kontrastowy.load()

    mn = ((255 + wsp_kontrastu) / 255) ** 2

    for i in range(obraz_kontrastowy.width):
        for j in range(obraz_kontrastowy.height):
            r, g, b = pixels[i, j]
            r = int(128 + (r - 128) * mn)
            g = int(128 + (g - 128) * mn)
            b = int(128 + (b - 128) * mn)
            pixels[i, j] = (r,g,b)

    return obraz_kontrastowy

#kontrast(obraz,100).show()

def transformacja_logarytmiczna(obraz):
    obraz_transformowany = obraz.copy()
    pixels = obraz_transformowany.load()

    for i in range(obraz_transformowany.width):
        for j in range(obraz_transformowany.height):
            r, g, b = pixels[i, j]
            r = int(255 * np.log(1 + r / 255))
            g = int(255 * np.log(1 + g / 255))
            b = int(255 * np.log(1 + b / 255))
            pixels[i, j] = (r,g,b)

    return obraz_transformowany

#transformacja_logarytmiczna(obraz).show()

def transformacja_gamma(obraz,gamma):
    obraz_transformowany = obraz.copy()
    pixels = obraz_transformowany.load()

    for i in range(obraz_transformowany.width):
        for j in range(obraz_transformowany.height):
            r, g, b = pixels[i, j]
            r = int((r/255)**(1/gamma)*255)
            g = int((g/255)**(1/gamma)*255)
            b = int((b/255)**(1/gamma)*255)
            pixels[i, j] = (r,g,b)

    return obraz_transformowany

#transformacja_gamma(obraz,.5).show()

#zadanie 6
def add_constant(image_array, constant):
    # Dodaj stałą do każdego piksela
    result_array = image_array + constant
    
    # Ogranicz wartości do zakresu 0-255
    result_array[result_array < 0] = 0
    result_array[result_array > 255] = 255
    
    # Konwertuj na typ uint8
    result_array = result_array.astype(np.uint8)
    
    return result_array

t = np.array(obraz,dtype='uint8')
obraz_wynik = t+100
obraz_wynik = Image.fromarray(obraz_wynik,"RGB")
obraz_wynik.show()
t2 = obraz.copy()
t2.point(lambda i: i+100).show()
Image.fromarray(add_constant(t,100)).show()
