from PIL import Image
import numpy as np


def random_key(width, height):
    """NumPy array of given size

    helper function
    return uint8 data type RGB noise to keep 8 bit's per channel
    """
    np_array = np.random.randint(0, 256, (height, width, 3))
    return np.array(np_array, dtype=np.uint8)


def split_pic(original_image, name_a="out_A.bmp", name_b="out_B.bmp"):
    """saving noise images

    outputs two noise files, both are needed to recover original.
    name_a and name_b determine the file format, eg. BMP
    using other than lossless bitmap formats may result
    in unexpected behaviour
    """
    input_img = Image.open(original_image)
    array_from_input_img = np.asarray(input_img, dtype=np.uint8)
    random_noise = random_key(input_img.size[0], input_img.size[1])
    subtracted_array = array_from_input_img - random_noise
    Image.fromarray(random_noise).save(name_a)  # img from noise map
    Image.fromarray(subtracted_array).save(name_b)  # img after subtraction


def join_pics(file_A, file_B, output_name="original.bmp"):
    """joins two files in one

    must be same pixel-size
    output_name determines the file format, eg. BMP
    order of input images is NOT important
    """
    input_a = Image.open(file_A)
    input_b = Image.open(file_B)
    array_from_input_a = np.asarray(input_a, dtype=np.uint8)
    array_from_input_b = np.asarray(input_b, dtype=np.uint8)
    add_array = array_from_input_a + array_from_input_b
    Image.fromarray(add_array).save(output_name)


# testing functions, original.bmp included in working directory
# uncomment next two lines to see how it works
#split_pic("original.bmp")
#join_pics("out_B.bmp", "out_A.bmp", "recovered_original.jpg")
