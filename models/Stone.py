"""
Module: stone

This module defines the abstract base class Stone, which represents a stone
object with a name and color.
Subclasses of Stone should implement the abstract method get_full_price().
"""
from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class Stone(ABC):
    """
    Class: Stone

    This class provides abstract methods that subclasses should implement
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def get_full_price(self):
        """
        Abstract method get_full_price
        :return: skip
        """
