from precious_stone import PreciousStone


def main():
    precious_stone = PreciousStone.get_instance()
    print(precious_stone)

    total_price = precious_stone.get_total_price()
    print("Total price of the stone", total_price)

    precious_stone.increase_clarity()
    print("Increased clarity:", precious_stone.clarity)

    precious_stone.increase_price(10)
    print("Total price per carat:", precious_stone.price_per_carat)

    precious_stone.get_instance()
    print(precious_stone.get_instance())


if __name__ == "__main__":
    main()
