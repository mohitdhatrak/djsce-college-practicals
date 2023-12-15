def heuristic(x):
    value = x
    return value


def hillclimb():
    grid_size = 4

    # grid to find maximum number using hill climb
    grid = [
        [1, 2, 3, 4],
        [5, 9, 6, 8],
        [7, 12, 10, 11],
        [13, 14, 15, 16],
    ]

    # local maxima issue in hill climb
    # grid = [
    #     [1, 2, 9, 4],
    #     [7, 3, 6, 8],
    #     [5, 4, 10, 11],
    #     [13, 14, 15, 16],
    # ]

    # start from top left
    position = [0, 0]
    max_val = float("-inf")

    while True:
        old_val = max_val
        x = position[0]  # row number
        y = position[1]  # column number

        possible_moves = [
            [x - 1, y],  # up
            [x + 1, y],  # down
            [x, y - 1],  # left
            [x, y + 1],  # right
            [x + 1, y + 1],  # right-down diagonal
            [x - 1, y - 1],  # left-up diagonal
            [x + 1, y - 1],  # left-down diagonal
            [x - 1, y + 1],  # right-up diagonal
        ]

        for x1, y1 in possible_moves:
            if 0 <= x1 < grid_size and 0 <= y1 < grid_size:
                val = heuristic(grid[x1][y1])

                if val > max_val:
                    print(f"Better value found: {val}")
                    max_val = val
                    position = [x1, y1]  # update position
                    # in hill climb, we don't backtrack, we just consider the better solution and move forward

        if old_val == max_val:
            print("No better value found for possible moves!")
            print("No improvement possible, so we stop the hill climb")
            break

    print(f"Max value (peak of hill) is {max_val} at position {position}")


hillclimb()
