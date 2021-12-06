import numpy as np
import queue

# Matrix visualized
#                 1  2  3  4  5  6  7  8  9
line1 = np.array([0, 0, 3, 0, 2, 0, 6, 0, 0])  # A
line2 = np.array([9, 0, 0, 3, 0, 5, 0, 0, 1])  # B
line3 = np.array([0, 0, 1, 8, 0, 6, 4, 0, 0])  # C
line4 = np.array([0, 0, 8, 1, 0, 2, 9, 0, 0])  # D
line5 = np.array([7, 0, 0, 0, 0, 0, 0, 0, 8])  # E
line6 = np.array([0, 0, 6, 7, 0, 8, 2, 0, 0])  # F
line7 = np.array([0, 0, 2, 6, 0, 9, 5, 0, 0])  # G
line8 = np.array([8, 0, 0, 2, 0, 3, 0, 0, 9])  # H
line9 = np.array([0, 0, 5, 0, 1, 0, 3, 0, 0])  # I

matrix = np.array([line1, line2, line3, line4, line5, line6, line7, line8, line9])

print("Sudoku problem:")
for value in range(9):
    print(matrix[value])


# def ac3(square9by9):  # Todo
#     q = queue.Queue()
#     if q.empty:
#         print("its empty")
#     print(square9by9)

def blockShaped(arr, nrows, ncols):
    h, w = arr.shape
    assert h % nrows == 0, f"{h} rows is not evenly divisible by {nrows}"
    assert w % ncols == 0, f"{w} cols is not evenly divisible by {ncols}"
    return (arr.reshape(h // nrows, nrows, -1, ncols)
            .swapaxes(1, 2)
            .reshape(-1, nrows, ncols))


SudokuTable = blockShaped(matrix, 3, 3)


def getNeighbors(valX, valY):
    listOfNeighbors = []
    listOfNeighbors.append(matrix[valX])
    listOfNeighbors.append(matrix[:, valY])
    if 0 <= valX < 3 and 3 > valY >= 0:
        listOfNeighbors.append(SudokuTable[0])
    if 0 <= valX < 3 and 6 > valY >= 3:
        listOfNeighbors.append(SudokuTable[1])
    if 0 <= valX < 3 and 9 > valY >= 6:
        listOfNeighbors.append(SudokuTable[2])
    if 3 <= valX < 6 and 3 > valY >= 0:
        listOfNeighbors.append(SudokuTable[3])
    if 3 <= valX < 6 and 6 > valY >= 3:
        listOfNeighbors.append(SudokuTable[4])
    if 3 <= valX < 6 and 9 > valY >= 6:
        listOfNeighbors.append(SudokuTable[5])
    if 6 <= valX < 9 and 3 > valY >= 0:
        listOfNeighbors.append(SudokuTable[6])
    if 6 <= valX < 9 and 6 > valY >= 3:
        listOfNeighbors.append(SudokuTable[7])
    if 6 <= valX < 9 and 9 > valY >= 6:
        listOfNeighbors.append(SudokuTable[8])
    return listOfNeighbors


print("----------------")
print("Solution to the Sudoku problem:")
