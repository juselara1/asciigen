from cv2 import cv2
import numpy as np
from numpy import ndarray as Array
from typing import List, Union

class Image(Array):

    def __new__(cls, values: Union[List, Array]):
        obj = np.asarray(values).view(cls)
        return obj

    @staticmethod
    def load_from_file(filename: str) -> "Image":
        return Image(cv2.imread(filename, 0))

    def resize(self, width: int, height: int) -> "Image":
        return Image(cv2.resize(self, (width, height)))

    def set_levels(self, n_levels: int) -> "Image":
        quantiles = np.quantile(
                self, np.linspace(0, 1, n_levels + 1)
                )
        intervals = [
                (quantiles[i], quantiles[i + 1])
                for i in range(n_levels)
                ]
        new_img = Image(np.zeros(self.shape, dtype=self.dtype))
        for i, interval in enumerate(intervals):
            new_img[(self >= interval[0]) & (self <= interval[1])] = i
        return new_img

    @property
    def height(self):
        return self.shape[0]

    @property
    def width(self):
        return self.shape[1]
