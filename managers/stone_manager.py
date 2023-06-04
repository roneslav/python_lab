"""
Module: stone_manager
"""
from decorators.decorators import logged  # pylint: disable=import-error
from exceptions.no_circle_stones_exception import NoCircleStonesException  # pylint: disable=import-error
from exceptions.no_green_stones_exception import NoGreenStonesException  # pylint: disable=import-error


class StoneManager:
    """
    Class: StoneManager

    This class provides all methods for managing stones
    """
    def __init__(self):
        self.stones = []

    def __len__(self):
        return len(self.stones)

    def __getitem__(self, index):
        return self.stones[index]

    def __iter__(self):
        return iter(self.stones)

    def add_in_list(self, stone):
        """
        Method: add_in_list
        :param stone: iterator for list stones
        :return: new stone to the list stones
        """
        self.stones.append(stone)

    @logged(NoGreenStonesException, mode = 'file')
    def find_stones_that_are_green(self):
        """
        Method: find_stones_that_are_green
        :return: only stones that are green
        """
        stones_that_are_green = list(filter(lambda stones: 'green' == stones.color, self.stones))
        if not stones_that_are_green:
            raise NoGreenStonesException("There are no green stones.")
        for stone in stones_that_are_green:
            print(stone)

    @logged(NoCircleStonesException, mode = 'file')
    def find_stones_that_are_circles(self):
        """
        Method: find_stones_that_are_circles
        :return: only stones that are circles
        """
        stones_that_are_circles = list(filter(lambda stones: 'circle' in stones.shape, self.stones))
        if not stones_that_are_circles:
            raise NoCircleStonesException("There are no circle stones.")
        for stone in stones_that_are_circles:
            print(stone)

    def in_list_full_price(self):
        """
        Method: in_list_full_price
        :return: list of full prices
        """
        result = [stone.get_full_price() for stone in self.stones]
        return result

    def find_index_of_objects(self, stones):  # pylint: disable=unused-argument
        """
        Method: find_index_of_objects
        :param stones:
        :return: index: object
        """
        result_obj = [f'{index}: {item}' for index, item in enumerate(self.stones)]
        return result_obj
