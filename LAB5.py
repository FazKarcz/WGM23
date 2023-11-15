from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

#ZADANIE 2
#                   NOTATKI
#Obraz 5 jest bardziej blady niż pierwszy obraz.
#Można powiedzieć że obraz1 ma dużo żywsze kolory.(Z jakiegoś powodu, obray ważą więcej niż ich orginał)
#Jednak nie ważnie XD trzeba beedzie sprawidzić funkcją porównującą obrazy. Póki co jedne obrazy,
#, mają kolory ciemniejsze drugie jaśniejsze. Po użyciu funkcji "Statystyki", obraz 1 i obraz 5 różnią się
#odchyleniem standardowym, oraz średnią.
im = Image.open('obraz.jpg')
h, w = im.size
im.save("obraz2.jpg")
im2 = Image.open("obraz2.jpg")
im2.save("obraz3.jpg")
im3 = Image.open("obraz3.jpg")
im3.save("obraz4.jpg")
im4 = Image.open("obraz4.jpg")
im4.save("obraz5.jpg")

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

#statystyki(im)
statystyki(im3)
print("-----------------------------------------------------------------")
statystyki(im4)
