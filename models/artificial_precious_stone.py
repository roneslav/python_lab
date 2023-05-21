from models.stone import stone


class artificial_precious_stone(stone):
    def __init__(self, name_of_laboratory, mass_in_grams, price_per_gram, color, shape, name):
        super().__init__(name, color)
        self.name_of_laboratory = name_of_laboratory
        self.mass_in_grams = mass_in_grams
        self.price_per_gram = price_per_gram
        self.color = color
        self.shape = shape

    def __str__(self):
        return f'Artificial precious stone: {self.name_of_laboratory},' \
               f' {self.mass_in_grams}, {self.price_per_gram}, {self.color}, {self.shape}, {self.name} '

    def get_full_price(self):
        full_price = self.mass_in_grams * self.price_per_gram
        return full_price
