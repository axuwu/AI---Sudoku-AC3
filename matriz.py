import numpy as np
import queue
#
# #                 1  2  3  4  5  6  7  8  9
# line1 = np.array([0, 0, 3, 0, 2, 0, 6, 0, 0])  # A
# line2 = np.array([9, 0, 0, 3, 0, 5, 0, 0, 1])  # B
# line3 = np.array([0, 0, 1, 8, 0, 6, 4, 0, 0])  # C
# line4 = np.array([0, 0, 8, 1, 0, 2, 9, 0, 0])  # D
# line5 = np.array([7, 0, 0, 0, 0, 0, 0, 0, 8])  # E
# line6 = np.array([0, 0, 6, 7, 0, 8, 2, 0, 0])  # F
# line7 = np.array([0, 0, 2, 6, 0, 9, 5, 0, 0])  # G
# line8 = np.array([8, 0, 0, 2, 0, 3, 0, 0, 9])  # H
# line9 = np.array([0, 0, 5, 0, 1, 0, 3, 0, 0])  # I
#
# matrix = np.array([line1, line2, line3, line4, line5, line6, line7, line8, line9])
#
# print("Sudoku problem:")
# for value in range(9):
#     print(matrix[value])
#
#
# def ac3(square9by9):  # Todo
#     q = queue.Queue()
#     if q.empty:
#         print("its empty")
#     print(square9by9)
#
#
# print("----------------")
# print("Solution to the Sudoku problem:")
# ac3(matrix)

rows = "123456789"
cols = "ABCDEFGHI"

def generate_coords(cols, rows):
    all_cells_coords = []

    # for A,B,C, ... ,H,I
    for col in cols:

        # for 1,2,3 ,... ,8,9
        for row in rows:
            # A1, A2, A3, ... , H8, H9
            new_coords = col + row
            all_cells_coords.append(new_coords)

    return all_cells_coords


matrix = generate_coords(cols, rows)

