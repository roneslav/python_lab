from models.Stone import Stone


class SemiPreciousStone(Stone):
    def __init__(self, name, color, clarity, carat, shape):
        super().__init__(name, color)
        self.clarity = clarity
        self.carat = carat
        self.shape = shape

    def __str__(self):
        return f'Semi Precious Stone: {self.name}, {self.color}, {self.clarity}, {self.carat}, {self.shape}'

    def get_full_price(self):
        pass
