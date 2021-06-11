from PIL import Image
import numpy as np

def nahodny_klic(vystup, sirka, vyska):

    pole = np.random.randint(0,256, (vyska,sirka,3))  
    pole = np.array(pole, dtype=np.uint8)
    klic = Image.fromarray(pole)
    klic.save(vystup)

# načtení vstupního obrazu jako pole
obraz1 = Image.open('vstup.jpg')
vstup = np.asarray(obraz1, dtype=np.uint8)

# vygenerování a uložení klíče podle rozměru vstupního obrazu
nahodny_klic('klic.bmp', obraz1.size[0], obraz1.size[1])

# načtení klíče jako pole
obraz2 = Image.open('klic.bmp')
klic = np.asarray(obraz2, dtype=np.uint8)

# zamčení obrazu sečtením vstupu a klíče
zamceno = vstup + klic
zamceno_img = Image.fromarray(zamceno)
zamceno_img.save('zamceno.bmp') # uložení zamčeného obrazu

# odemčení odečtením klíče od zamčeného obrazu
odemceno = zamceno - klic
odemceno_img = Image.fromarray(odemceno)
odemceno_img.save('odemceno.bmp') # uložení obnoveného obrazu