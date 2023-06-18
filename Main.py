"""
Module main
Includes main method to start the program
"""


from models.precious_stone import PreciousStone
from models.artificial_precious_stone import ArtificialPreciousStone
from models.jewelry_stone import JewelryStone
from models.semi_precious_stone import SemiPreciousStone
from managers.stone_manager import StoneManager


def main():
    """
    Main() method
    :return: all results of methods that we need
    """
    print('All stones:')
    stone_manager = StoneManager()
    stone_manager.add_in_list(PreciousStone(55, 4, 25, 'blue', 'square', 'Diamond'))
#    stone_manager.add_in_list(PreciousStone(100, 5, 35, 'green', 'circle', 'Ruby'))
#    stone_manager.add_in_list(ArtificialPreciousStone('BioLab', 5, 20, 'green', 'circle', 'Cubic'))
    stone_manager.add_in_list(ArtificialPreciousStone('DeltaLab', 4, 25, 'pink', 'trapezium', 'Al'))
    stone_manager.add_in_list(JewelryStone('Pearl', 'red', 5, 'square'))
#    stone_manager.add_in_list(JewelryStone('Opal', 'green', 3, 'circle'))
#   stone_manager.add_in_list(SemiPreciousStone('Amethyst', 'pink', 5, 25, 'circle'))
#    stone_manager.add_in_list(SemiPreciousStone('Aquamarine', 'green', 4, 100, 'trapezium'))
    for stone in stone_manager.stones:
        print(stone)

    print('Stones that are green:')
    stone_manager.find_stones_that_are_green()

    print('Stones that are circles:')
    stone_manager.find_stones_that_are_circles()

    print('All full prices:')
    result = stone_manager.in_list_full_price()
    for price in result:
        print(price)

    indexes = stone_manager.find_index_of_objects(stone_manager.stones)
    for item in indexes:
        print(item)

    gluing = list(zip(stone_manager.in_list_full_price()))
    print(gluing)

    for stone_attributes in stone_manager.stones:
        attributes_int = stone_attributes.attributes_by_type(int)
        print('Int attributes:', attributes_int)

    for stone_attributes in stone_manager.stones:
        attributes_str = stone_attributes.attributes_by_type(str)
        print('Str attributes:', attributes_str)

#    conditions_result = stone_manager.check_conditions(lambda l: l.clarity > 4)
#    print("All conditions satisfied:", conditions_result["all"])
#    print("Any condition satisfied:", conditions_result["any"])


if __name__ == '__main__':
    main()

