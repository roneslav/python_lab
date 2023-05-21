from abc import abstractmethod


class stone:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @abstractmethod
    def get_full_price(self):
        pass
