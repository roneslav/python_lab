class PreciousStone:
    def __init__(self, name="ros", carat=5, color="kfkf", clarity=3, price_per_carat=55):
        self.name = name
        self.carat = carat
        self.color = color
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    def __str__(self):
        return f'Precious Stone: {self.name}, {self.carat}, {self.color}, {self.clarity}, {self.price_per_carat} '

    def get_total_price(self):
        total_price = self.carat * self.price_per_carat
        return total_price

    def increase_clarity(self):
        increased_clarity = self.clarity + 1
        return increased_clarity

    def increase_price(self, percentage):
        increased_price = self.price_per_carat + ((percentage / 100) * self.price_per_carat)
        return increased_price

    @staticmethod
    def get_instance():
        if not PreciousStone.instance:
            PreciousStone.instance = PreciousStone()
        return PreciousStone.instance
