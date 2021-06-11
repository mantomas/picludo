from PIL import Image
import numpy as np


def random_key(width, height):
    """NumPy array of given size

    return uint8 data type to keep 8 bit's per channel
    """
    np_array = np.random.randint(0, 256, (height, width, 3))
    return np.array(np_array, dtype=np.uint8)


def split_pic(original_image, name_a="out_A.bmp", name_b="out_B.bmp"):
    """saving two noise images

    
    """
    input_img = Image.open(original_image)
    array_from_input_img = np.asarray(input_img, dtype=np.uint8)
    random_noise = random_key(input_img.size[0], input_img.size[1])
    subtracted_array = array_from_input_img - random_noise
    Image.fromarray(random_noise).save(name_a)  # img from noise map
    Image.fromarray(subtracted_array).save(name_b)  # img after subtraction



def join_pics():

    return None


# vygenerování a uložení klíče podle rozměru vstupního obrazu
random_key("klic.bmp", obraz1.size[0], obraz1.size[1])

# načtení klíče jako pole
obraz2 = Image.open("klic.bmp")
klic = np.asarray(obraz2, dtype=np.uint8)

# zamčení obrazu sečtením vstupu a klíče
zamceno = vstup + klic
zamceno_img = Image.fromarray(zamceno)
zamceno_img.save("zamceno.bmp")  # uložení zamčeného obrazu

# odemčení odečtením klíče od zamčeného obrazu
odemceno = zamceno - klic
odemceno_img = Image.fromarray(odemceno)
odemceno_img.save("odemceno.bmp")  # uložení obnoveného obrazu
