"""
Module precious_stone
This module provides managing stones like a Precious Stones
"""
from models.stone import Stone


class PreciousStone(Stone):
    """
    Class PreciousStone
    Managing methods that were required in previous lab and get_full_price
    """
    # pylint: disable=too-many-arguments
    def __init__(self, carat, clarity, price_per_carat, color, shape, name):
        """
        :param carat:The weight of the precious stone in carats
        :param clarity:The clarity grade of the precious stone.
        :param price_per_carat:The price per carat of the precious stone.
        :param color:The color of the precious stone.
        :param shape:The shape of the precious stone.
        :param name:The name of the precious stone.
        """
        super().__init__(name, color)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat
        self.shape = shape

    def __str__(self):
        return f'Precious Stone: Carat: {self.carat}, Clarity: {self.clarity}, ' \
               f'Price per carat: {self.price_per_carat},' \
               f' Color: {self.color}, Shape: {self.shape}, Name: {self.name} '

    def get_total_price(self):
        """
        Method get_total_price
        :return: total_price = self.carat * self.price_per_carat
        """
        total_price = self.carat * self.price_per_carat
        return total_price

    def increase_clarity(self):
        """
        Method increase_clarity
        :return: increased_clarity = self.clarity + 1
        """
        increased_clarity = self.clarity + 1
        return increased_clarity

    def increase_price(self, percentage):
        """
        Method increase_price
        :param percentage: The percentage by which to increase the price.
        :return:The increased price per carat.
        """
        increased_price = self.price_per_carat + ((percentage / 100) * self.price_per_carat)
        return increased_price

    def get_full_price(self):
        """
        Method get_full_price
        :return: full_price = self.carat * self.price_per_carat

        """
        full_price = self.carat * self.price_per_carat
        return full_price

