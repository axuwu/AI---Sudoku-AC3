import queue

# Matrix visualized
#          1  2  3  4  5  6  7  8  9
matrix = [[0, 0, 3, 0, 2, 0, 6, 0, 0],  # A
          [9, 0, 0, 3, 0, 5, 0, 0, 1],  # B
          [0, 0, 1, 8, 0, 6, 4, 0, 0],  # C
          [0, 0, 8, 1, 0, 2, 9, 0, 0],  # D
          [7, 0, 0, 0, 0, 0, 0, 0, 8],  # E
          [0, 0, 6, 7, 0, 8, 2, 0, 0],  # F
          [0, 0, 2, 6, 0, 9, 5, 0, 0],  # G
          [8, 0, 0, 2, 0, 3, 0, 0, 9],  # H
          [0, 0, 5, 0, 1, 0, 3, 0, 0]]  # I


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


# Function to get both coordinates x and y from a cell of Sudoku
def getCoord(cell):
    coordX = cell[0]
    coordY = cell[1]
    return coordX, coordY


# Function Arc Reduce
# Given a constraint remove from the domain D_c1 all values that have no support in D_c2
# Returns true if it the domain of c1 gets revised
def revise(constraint, cell1, cell2):
    revised = False
    # 1st cell
    row1, column1 = getCoord(cell1)
    # 2nd cell
    row2, column2 = getCoord(cell2)

    # find a value vy in D(y) such that vx and vy satisfy the constraint c2(x, y)

    # i as in possible values of the domain
    for i in constraint[1][constraint[0].index(cell1)]:
        value = [i]
        
        #arc reducing
        # checks the size of the domain  -> if the size>1 then the domain is still isn't revised aka unoccupied cell (0)
        # checks the cells themselves -> if the cell1 is same as cell2
        if (len(constraint[1][constraint[0].index([row2, column2])]) == 1) and \
                (value == constraint[1][constraint[0].index([row2, column2])]):
            # removes the given value of Cell2's Domain in the Domain of Cell1
            constraint[1][constraint[0].index([row1, column1])].pop(constraint[1][constraint[0].
                                                                    index([row1, column1])].index(value[0]))

            revised = True

    return revised


# --------------------------------------------


csp = fillDomain()  # csp = [[cell[x,y]], [domain[...]]]

# blocks are cells
block1 = [0, 0]
block2 = [0, 1]
block3 = [0, 2

# Example: will say FALSE bc he has same domain of 1st cell
print("domains are same then the revise is: ", revise(csp, block1, block2))
# Example: will say TRUE bc he will remove the number 3 from the domain of 1st cell
print("domains are different then the revise is: ", revise(csp, block1, block3))
