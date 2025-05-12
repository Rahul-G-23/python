def print_character_grid(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
    example_grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['.', '.', 'O', 'O', 'O', 'O'],
        ['.', '.', '.', 'O', 'O', 'O']
    ]

    print("Example Grid:")
    print_character_grid(example_grid)

    custom_grid = [
        ['#', '#', '#'],
        ['#', ' ', '#'],
        ['#', '#', '#']
    ]

    print("\nCustom Grid:")
    print_character_grid(custom_grid)

    text_grid = [
        ['P', 'y', 't', 'h', 'o', 'n'],
        ['i', 's', ' ', 'f', 'u', 'n'],
        ['!', '!', '!', ' ', ':', ')']
    ]

    print("\nText Grid:")
    print_character_grid(text_grid)
