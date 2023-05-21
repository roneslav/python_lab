from models.Stone import Stone


class JewelryStone(Stone):
    def __init__(self, name, color, carat, shape):
        super().__init__(name, color)
        self.carat = carat
        self.shape = shape

    def __str__(self):
        return f'Jewelry Stone: {self.name}, {self.color}, {self.carat}, {self.shape}'

    def get_full_price(self):
        pass
