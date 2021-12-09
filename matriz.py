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
matrix = np.array([line1,
                   line2,
                   line3,
                   line4,
                   line5,
                   line6,
                   line7,
                   line8,
                   line9])


# Method to fill the domain of each cell from the Sudoku
# Returns a 2d-Array that:
# [0] = cell (coordinateX, coordinateY)
# [1] = domain
def fillDomain():
    doubleArray = [[], []]
    for rows in range(9):
        for columns in range(9):
            if matrix[rows][columns] == 0:
                doubleArray[0].append([rows, columns])
                doubleArray[1].append([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                doubleArray[0].append([rows, columns])
                doubleArray[1].append([matrix[rows][columns]])
    return doubleArray


# Function to get (all 20) neighbors from coordinate (coordX, coordY) of the Sudoku Table
# 8 neighbors from the Horizontal Line
# 8 neighbors from the Vertical line
# 4 neighbors from the Same Square
def getNeighbors(coordX, coordY):
    listOfNeighbors = []
    for valueX in range(9):
        for valueY in range(9):
            if (valueX == coordX) and (valueY == coordY):  # ignores itself since is itself
                pass
            else:
                if valueX == coordX or valueY == coordY or sameSquare(coordX, coordY, valueX, valueY):
                    listOfNeighbors.append([valueX, valueY])  # the duo (x, y) aka neighbor are added to the list
    return listOfNeighbors


# Function to check if values (x, y) are from the same Square as coordinate (coordX, coordY)
def sameSquare(coordX, coordY, valueX, valueY):
    if (0 <= coordX < 3) and (0 <= coordY < 3) and (0 <= valueX < 3) and (0 <= valueY < 3):
        # Square 1
        return True
    elif (0 <= coordX < 3) and (3 <= coordY < 6) and (0 <= valueX < 3) and (3 <= valueY < 6):
        # Square 2
        return True
    elif (0 <= coordX < 3) and (6 <= coordY < 9) and (0 <= valueX < 3) and (6 <= valueY < 9):
        # Square 3
        return True
    elif (3 <= coordX < 6) and (0 <= coordY < 3) and (3 <= valueX < 6) and (0 <= valueY < 3):
        # Square 4
        return True
    elif (3 <= coordX < 6) and (3 <= coordY < 6) and (3 <= valueX < 6) and (3 <= valueY < 6):
        # Square 5
        return True
    elif (3 <= coordX < 6) and (6 <= coordY < 9) and (3 <= valueX < 6) and (6 <= valueY < 9):
        # Square 6
        return True
    elif (6 <= coordX < 9) and (0 <= coordY < 3) and (6 <= valueX < 9) and (0 <= valueY < 3):
        # Square 7
        return True
    elif (6 <= coordX < 9) and (3 <= coordY < 6) and (6 <= valueX < 9) and (3 <= valueY < 6):
        # Square 8
        return True
    elif (6 <= coordX < 9) and (6 <= coordY < 9) and (6 <= valueX < 9) and (6 <= valueY < 9):
        # Square 9
        return True
    else:
        return False


# Function to get either coordinate x or y from a block of Sudoku
def getCoord(block, coord):
    gottenNumber = 0
    if (coord == "x") and (len(block) == 2):
        gottenNumber = block[0]
    elif (coord == "y") and (len(block) == 2):
        gottenNumber = block[1]
    else:
        return 0
    return gottenNumber


# arc reducing
# checks the size of the cells and compares them
# if the size isn't 1 then the domain is still large
def checkSize(constraint, cell1, cell2):
    # 1st cell
    row1 = getCoord(cell1, "x")
    column1 = getCoord(cell1, "y")
    # 2nd cell
    row2 = getCoord(cell2, "x")
    column2 = getCoord(cell2, "y")
    aux = [row1, column1]
    # csp = [ [ cell[coordX, coordY] ], [ domain[...] ] ]
    if len(constraint[1][constraint[0].index([row2, column2])]) == 1:
        return True
    return False


# arc reducing
# checks the cells themselves
# if the cell1 is same as cell2
def checkCell(constraint, cell1, cell2):
    # 1st cell
    row1 = getCoord(cell1, "x")
    column1 = getCoord(cell1, "y")
    # 2nd cell
    row2 = getCoord(cell2, "x")
    column2 = getCoord(cell2, "y")
    aux = [row1, column1]
    # csp = [ [ cell[coordX, coordY] ], [ domain[...] ] ]
    for i in constraint[1][constraint[0].index(aux)]:  # iterates the domain of the cell
        i = [i]
        if len(constraint[1][constraint[0].index([row2, column2])]) == 1:
            return True
    return False


# Function Revise
# Given constraint C_ij remove from the domain D_i all values that have no support in D_j
# returns true if we revise the domain of i
def revise(constraint, cell1, cell2):
    # boolean flag
    revised = False

    # find a value vy in D(y) such that vx and vy satisfy the constraint R2(x, y)
    if (checkSize(constraint, cell1, cell2)) and (checkCell(constraint, cell1, cell2)):
        # TODO: removing domains
        revised = True
    return revised


csp = fillDomain()  # csp = [[cell[x,y]], [domain[...]]]

# blocks are cells
block1 = [0, 0]
block2 = [0, 1]
block3 = [0, 2]
# Example: will say no bc he has same domain of 1st cell
print("domains are same then the revise is: ", revise(csp, block1, block2))
# Example: will say yes bc he will remove the number 3 from the domain of 1st cell
print("domains are different then the revise is: ", revise(csp, block1, block3))
