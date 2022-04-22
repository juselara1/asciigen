import numpy as np
from numpy import ndarray as Array
from typing import List

class ColorScale(Array):

    def __new__(cls, values: List[str]) -> "ColorScale":
        obj = np.asarray(values).view(cls)
        return obj

    @staticmethod
    def load_from_file(filename: str) -> "ColorScale":
        with open(filename, 'r') as f:
            data = f.read()
        return ColorScale([character for character in data])

    @staticmethod
    def load(values: List[str]) -> "ColorScale":
        return ColorScale(values)
