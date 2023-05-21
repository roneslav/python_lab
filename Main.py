from models.PreciousStone import PreciousStone
from models.ArtificialPreciousStone import ArtificialPreciousStone
from managers.StoneManager import StoneManager
from models.JewelryStone import JewelryStone
from models.SemiPreciousStone import SemiPreciousStone


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
