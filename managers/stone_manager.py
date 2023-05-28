"""
Module: stone_manager

This module provides a StoneManager class for managing stones
"""
from models.stone import Stone


def find_index_of_objects(stones):
    result = [f'{index}: {item}' for index, item in enumerate(stones)]
    return result


class StoneManager(Stone):
    """
    Class: StoneManager

    This class provides all methods for managing stones
    """

    def __len__(self):
        return len(self)

    def __getitem__(self, index):
        return self[index]

    def __iter__(self):
        return iter(self)

    def get_full_price(self):
        """
        Method: get_full_price
        :return: pass
        """

    def __init__(self):
        self.stones = []

    def add_in_list(self, stone):
        """
        Method: add_in_list
        :param stone: iterator for list stones
        :return: new stone to the list stones
        """
        self.stones.append(stone)

    def find_stones_that_are_green(self):
        """
        Method: find_stones_that_are_green
        :return: only stones that are green
        """
        stones_that_are_green = list(filter(lambda stones: 'green' == stones.color, self.stones))
        for stone in stones_that_are_green:
            print(stone)

    def find_stones_that_are_circles(self):
        """
        Method: find_stones_that_are_circles
        :return: only stones that are circles
        """
        stones_that_are_circles = list(filter(lambda stones: 'circle' in stones.shape, self.stones))
        for stone in stones_that_are_circles:
            print(stone)

    def in_list_full_price(self):
        result = [stone.get_full_price() for stone in self.stones]
        return result

    def all(self):
        return all(stone.clarity > 8 for stone in self.stones)

    def any(self):
        return any(stone.clarity > 8 for stone in self.stones)

