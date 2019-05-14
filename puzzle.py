"""
This file solves the puzzle
Author: Bruno Lerner
"""

def filter_zero_cells(cell):
    return 0 in cell

def filter_cells_with_certain_number(number):
    def filter_cells(cell):
        return number in cell
    return filter_cells

def is_zero_dupicated(cell):
    temp_cell = list(cell)
    number_of_zeros = 0
    while 0 in temp_cell:
        number_of_zeros += 1
        temp_cell.remove(0)

    return number_of_zeros == 2

def find_neighbor_cell(number, zero_direction, borders_cells):
    neighbor_cells = []
    for possible_neighbor in borders_cells:
        index_of_zero_appearance = possible_neighbor.index(0)
        if possible_neighbor[(index_of_zero_appearance - zero_direction) % len(possible_neighbor)] == number:
            neighbor_cells.append(possible_neighbor)
    return neighbor_cells

def solve_puzzle(puzzle):
    solution = []

    # Find out the border cells and corner cells
    borders_cells = list(filter(filter_zero_cells, puzzle))
    corner_cells = list(filter(is_zero_dupicated, puzzle))
    not_corner_border_cells = [item for item in borders_cells if item not in corner_cells]

    root_cell = corner_cells[0]
    solution.append(root_cell)

    possible_neighbors = find_neighbor_cell(17, 1, not_corner_border_cells)
    while len(possible_neighbors) != 0:
        current_cell = solution[-1]
        index_of_first_number = (current_cell.index(0) + 1) % 4 if current_cell[(current_cell.index(0) + 1) % 4] != 0 \
            else (current_cell.index(0) + 2) % 4
        possible_neighbors = find_neighbor_cell(current_cell[index_of_first_number], 1, not_corner_border_cells)
        print(solution)
        solution.append(possible_neighbors[0])




def main():
    # Getting the txt file and populating data structure
    f = open("puzzle.txt", "r")
    raw_puzzle = f.readline()
    f.close()

    puzzle = [x[x.index("[")+1:x.index("]")].split(",") for x in raw_puzzle.split(';')]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            puzzle[i][j] = int(puzzle[i][j])
    puzzle = [tuple(x) for x in puzzle]

    solve_puzzle(puzzle)



if __name__ == "__main__":
    main()
