"""
Module artificial_precious_stone
This module provides managing stones like an Artificial Precious Stones
"""
from models.stone import Stone


class ArtificialPreciousStone(Stone):
    """
    Class ArtificialPreciousStone
    Managing an abstract method get_full_price
    """

    # pylint: disable=too-many-arguments
    def __init__(self, name_of_laboratory, mass_in_grams, price_per_gram, color, shape, name):
        """
        Constructor
        :param name_of_laboratory: The name of the laboratory that created the stone.
        :param mass_in_grams:The mass of the artificial precious stone in grams.
        :param price_per_gram:The price per gram of the artificial precious stone.
        :param color:The color of the artificial precious stone.
        :param shape:The shape of the artificial precious stone.
        :param name:The name of the artificial precious stone.
        """
        super().__init__(name, color)
        self.name_of_laboratory = name_of_laboratory
        self.mass_in_grams = mass_in_grams
        self.price_per_gram = price_per_gram
        self.color = color
        self.shape = shape

    def __str__(self):
        return f'Artificial precious stone: {self.name_of_laboratory},' \
               f' {self.mass_in_grams}, {self.price_per_gram}, ' \
               f' {self.color}, {self.shape}, {self.name} '

    def get_full_price(self):
        """
        Method get_full_price
        :return:ull_price = self.mass_in_grams * self.price_per_gram

        """
        full_price = self.mass_in_grams * self.price_per_gram
        return full_price
