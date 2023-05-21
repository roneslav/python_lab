from models.precious_stone import precious_stone
from models.artificial_precious_stone import artificial_precious_stone
from managers.stone_manager import stone_manager
from models.jewelry_stone import jewelry_stone
from models.semi_precious_stone import semi_precious_stone


def main():
    print('All stones:')
    stone_manager = stone_manager()
    stone_manager.add_in_list(precious_stone(55, 4, 25, 'blue', 'square', 'Diamond'))
    stone_manager.add_in_list(precious_stone(100, 5, 35, 'green', 'circle', 'Ruby'))
    stone_manager.add_in_list(artificial_precious_stone('BioLab', 5, 20, 'green', 'circle', 'Cubic Zirconia'))
    stone_manager.add_in_list(artificial_precious_stone('DeltaLab', 4, 25, 'pink', 'trapezium', 'Moissanite'))
    stone_manager.add_in_list(jewelry_stone('Pearl', 'red', 5, 'square'))
    stone_manager.add_in_list(jewelry_stone('Opal', 'green', 3, 'circle'))
    stone_manager.add_in_list(semi_precious_stone('Amethyst', 'pink', 5, 25, 'circle'))
    stone_manager.add_in_list(semi_precious_stone('Aquamarine', 'green', 4, 100, 'trapezium'))
    for stone in stone_manager.stones:
        print(stone)

    print('Stones that are green:')
    stone_manager.find_stones_that_are_green()

    print('Stones that are circles:')
    stone_manager.find_stones_that_are_circles()


if __name__ == '__main__':
    main()
