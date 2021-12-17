import os
import numpy
from pathlib import Path
from ..picludo import Picludo


def test_random_key():
    """
    Given field size to method random_key()

    assert that returned object is:
        numpy.ndarray type
        propper shape of the array
        single RGB value is type numpy.uint8
    """
    data = Picludo.random_key(100, 100)
    assert isinstance(data, numpy.ndarray)
    assert data.shape == (100, 100, 3)
    assert isinstance(data[0][0][0], numpy.uint8)


def test_split_image():
    """
    Given input image to method split_image()

    assert:
        two output files exist after execution
    """
    Picludo.split_pic("original.bmp")
    file_1 = Path("out_A.bmp")
    file_2 = Path("out_B.bmp")
    assert file_1.is_file()
    assert file_2.is_file()


def test_join_pics():
    """
    Given two noise images

    assert:
        new joined file is created
    """
    Picludo.join_pics("out_A.bmp", "out_B.bmp", "test_out.bmp")
    file_out = Path("test_out.bmp")
    assert file_out.is_file()
    try:
        os.remove("out_A.bmp")
        os.remove("out_B.bmp")
        os.remove("test_out.bmp")
    except Exception:
        pass
