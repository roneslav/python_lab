"""
Module semi_precious_stone
This module provides managing stones like a Semi Precious Stones
"""
from models.stone import Stone


class SemiPreciousStone(Stone):
    """
    Class SemipreciousStone
    Managing constructor and method get_full_price
    """

    # pylint: disable=too-many-arguments
    def __init__(self, name, color, clarity, carat, shape):
        super().__init__(name, color)
        self.clarity = clarity
        self.carat = carat
        self.shape = shape

    def __str__(self):
        return f'Semi Precious Stone: Name: {self.name}, Color: {self.color}, ' \
               f' Clarity: {self.clarity}, Carat: {self.carat}, Shape: {self.shape}'

    def get_full_price(self):
        """
        Method get_full_price
        :return: pass
        """
