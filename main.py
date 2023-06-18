from models.precious_stone import PreciousStone
from models.artificial_precious_stone import ArtificialPreciousStone
from managers.stone_manager import StoneManager
from models.jewelry_stone import JewelryStone
from models.semi_precious_stone import SemiPreciousStone


def main():
    print('All stones:')
    stone_manager = StoneManager()
    stone_manager.add_in_list(PreciousStone(55, 4, 25, 'blue', 'square', 'Diamond'))
    stone_manager.add_in_list(PreciousStone(100, 5, 35, 'green', 'circle', 'Ruby'))
    stone_manager.add_in_list(ArtificialPreciousStone('BioLab', 5, 20, 'green', 'circle', 'Cubic Zirconia'))
    stone_manager.add_in_list(ArtificialPreciousStone('DeltaLab', 4, 25, 'pink', 'trapezium', 'Moissanite'))
    stone_manager.add_in_list(JewelryStone('Pearl', 'red', 5, 'square'))
    stone_manager.add_in_list(JewelryStone('Opal', 'green', 3, 'circle'))
    stone_manager.add_in_list(SemiPreciousStone('Amethyst', 'pink', 5, 25, 'circle'))
    stone_manager.add_in_list(SemiPreciousStone('Aquamarine', 'green', 4, 100, 'trapezium'))
    for stone in stone_manager.stones:
        print(stone)

    print('Stones that are green:')
    stone_manager.find_stones_that_are_green()

    print('Stones that are circles:')
    stone_manager.find_stones_that_are_circles()


if __name__ == '__main__':
    main()
