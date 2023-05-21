from models.stone import stone


class precious_stone(Stone):
    def __init__(self, carat, clarity, price_per_carat, color, shape, name):
        super().__init__(name, color)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat
        self.shape = shape

    def __str__(self):
        return f'Precious Stone: {self.carat}, {self.clarity}, {self.price_per_carat},' \
               f' {self.color}, {self.shape}, {self.name} '

    def get_total_price(self):
        total_price = self.carat * self.price_per_carat
        return total_price

    def increase_clarity(self):
        increased_clarity = self.clarity + 1
        return increased_clarity

    def increase_price(self, percentage):
        increased_price = self.price_per_carat + ((percentage / 100) * self.price_per_carat)
        return increased_price

    def get_full_price(self):
        full_price = self.carat * self.price_per_carat
        return full_price
