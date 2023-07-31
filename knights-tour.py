def create_board(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    return board

# moves the knight can make
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]

def create_solution(n):
    solution = [[-1 for _ in range(n)] for _ in range(n)]
    # we start from the (0, 0) positon
    solution[0][0] = 0
    return solution
