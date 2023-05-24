"""
Module jewelry_stone
This module provides managing stones like a Jewelry Stones
"""
from models.stone import Stone


class JewelryStone(Stone):
    """
    Class JewelryStone
    Managing constructor and method get_full_price
    """
    def __init__(self, name, color, carat, shape):
        super().__init__(name, color)
        self.carat = carat
        self.shape = shape

    def __str__(self):
        return f'Jewelry Stone: {self.name}, {self.color}, {self.carat}, {self.shape}'

    def get_full_price(self):
        """
        Method get_full_price
        :return: pass
        """
