from PIL import Image
import numpy as np

# DANE TABLICY
print("----------Dane Inicjaly----------")
inicjaly = Image.open("Inicjaly.bmp")
print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("typ danych tablicy", t_inicjaly.dtype)
print("rozmiar tablicy", t_inicjaly.shape)


# ZAD1
def rysuj_ramke_w_obrazie(obraz, grub):  # Dodac jeszcze paski na dół i na grórę
    tab_obraz = np.asarray(obraz) * 1  # wczytywanie jako int
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0
    tab = tab_obraz.astype(bool)  # zapisanie tablicy w typie bool
    return Image.fromarray(tab)


inicjaly_rammka = rysuj_ramke_w_obrazie(inicjaly, 5)
inicjaly_rammka.show()
