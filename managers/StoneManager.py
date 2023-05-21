from models.Stone import Stone


class StoneManager(Stone):
    def get_full_price(self):
        pass

    def __init__(self):
        self.stones = []

    def stones(self):
        return self.stones

    def add_in_list(self, stone):
        self.stones.append(stone)

    def find_stones_that_are_green(self):
        stones_that_are_green = list(filter(lambda stones: 'green' in stones.color, self.stones))
        for stone in stones_that_are_green:
            print(stone)

    def find_stones_that_are_circles(self):
        stones_that_are_circles = list(filter(lambda stones: 'circle' in stones.shape, self.stones))
        for stone in stones_that_are_circles:
            print(stone)
