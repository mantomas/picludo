import numpy
from ..picludo import Picludo


def test_random_key():
    """
    Create Picludo factory
    Given field size to function random_key()

    assert that returned object is:
        numpy.ndarray type
        propper shape of the array
        single RGB value is type numpy.uint8
    """
    factory = Picludo()
    data = factory.random_key(100, 100)
    assert isinstance(data, numpy.ndarray)
    assert data.shape == (100, 100, 3)
    assert isinstance(data[0][0][0], numpy.uint8)
