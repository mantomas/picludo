from PIL import Image
import numpy as np


class Picludo:
    """Picludo object for encrypt and decript images using noise

    Depends on:
        Pillow - open and save images
        Numpy - create and manipulate noise maps
    
    Methods:
        random_key(self, int, int)
        split_pic(self, image_path, name_a, name_b)
        join_pics(self, imageA_path, imageB_path, output_name)
    """
    def __init__(self):
        pass


    def random_key(self, width, height):
        """NumPy array of given size

        helper function
        return uint8 data type RGB noise to keep 8 bit's per channel
        """
        self.width = width
        self.height = height
        np_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        return np_array


    def split_pic(self, original_image, name_a="out_A.bmp", name_b="out_B.bmp"):
        """saving noise images

        outputs two noise files, both are needed to recover original.
        name_a and name_b determine the file format, eg. BMP
        using other than lossless bitmap formats may result
        in unexpected behaviour
        """
        input_img = Image.open(original_image)
        array_from_input_img = np.asarray(input_img, dtype=np.uint8)
        random_noise = self.random_key(input_img.size[0], input_img.size[1])
        subtracted_array = array_from_input_img - random_noise
        Image.fromarray(random_noise).save(name_a)  # img from noise map
        Image.fromarray(subtracted_array).save(name_b)  # img after subtraction


    def join_pics(self, file_A, file_B, output_name="recovered.bmp"):
        """joins two files in one

        must be same pixel-size
        output_name determines the file format, eg. BMP
        order of input images is NOT important
        """
        try:  # avoid different image sizes
            input_a = Image.open(file_A)
            input_b = Image.open(file_B)
            array_from_input_a = np.asarray(input_a, dtype=np.uint8)
            array_from_input_b = np.asarray(input_b, dtype=np.uint8)
            add_array = array_from_input_a + array_from_input_b
            Image.fromarray(add_array).save(output_name)
        except ValueError:
            pass


# testing functions, original.bmp included in working directory
# uncomment next lines to see how it works

#factory = Picludo()
#factory.split_pic("original.bmp")
#factory.join_pics("out_B.bmp", "out_A.bmp", "recovered_original.jpg")
