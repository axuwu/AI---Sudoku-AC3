import queue
import pandas as pd

# Matrix visualized
matrix = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
          [9, 0, 0, 3, 0, 5, 0, 0, 1],
          [0, 0, 1, 8, 0, 6, 4, 0, 0],
          [0, 0, 8, 1, 0, 2, 9, 0, 0],
          [7, 0, 0, 0, 0, 0, 0, 0, 8],
          [0, 0, 6, 7, 0, 8, 2, 0, 0],
          [0, 0, 2, 6, 0, 9, 5, 0, 0],
          [8, 0, 0, 2, 0, 3, 0, 0, 9],
          [0, 0, 5, 0, 1, 0, 3, 0, 0]]


# Method to fill the domain of each cell from the Sudoku
# Returns a 2d-Array that:
# [0] = cell (coordinateX, coordinateY)
# [1] = domain
def fillDomain(sudoku):
    constraint = ([[], []])
    for rows in range(9):
        for columns in range(9):
            if sudoku[rows][columns] == 0:
                # np.append
                constraint[0].append([rows, columns])
                constraint[1].append([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                constraint[0].append([rows, columns])
                constraint[1].append([sudoku[rows][columns]])
    return constraint


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


# Function to fill a queue with arcs
def fill_arc_queue(arcQueue):
    # Iterating in 1st cell
    for rowA in range(9):
        for colsA in range(9):
            # Iterating in 2nd cell
            for rowB in range(9):
                for colsB in range(9):
                    # Ignores if they are in the same cell coordinate (one cell can't be an arc of itself)
                    if (rowA == rowB) and (colsA == colsB):
                        pass
                    else:
                        # checks if they have either they are in the same row or columns or square
                        if (rowA == rowB) or (colsA == colsB) or (sameSquare(rowA, colsA, rowB, colsB)):
                            arcQueue.put([[rowA, colsA], [rowB, colsB]])


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
# Given a constraint remove a value from Cell2's Domain that is contained in Cell1's Domain
# only if they are Occupied cell (=/= 0)
# Returns true if it the domain of cell1 gets revised
def revise(constraint, cell1, cell2):
    revised = False
    # 1st cell
    row1, column1 = getCoord(cell1)
    # 2nd cell
    row2, column2 = getCoord(cell2)

    # i as in possible values of the domain
    for i in constraint[1][constraint[0].index(cell1)]:
        value = [i]

        # arc reducing
        # checks the size of the domain -> if the size>1 then the domain is still isn't revised aka unoccupied cell (0)
        # checks the cells themselves -> if the cell1 is same as cell2
        if (len(constraint[1][constraint[0].index([row2, column2])]) == 1) and \
                (value == constraint[1][constraint[0].index([row2, column2])]):
            # removes the given value of Cell2's Domain in the Domain of Cell1
            constraint[1][constraint[0].index([row1, column1])].pop(constraint[1][constraint[0].
                                                                    index([row1, column1])].index(value[0]))

            revised = True

    return revised


# Function that receives a unsolved sudoku and returns it solved
def ac3(sudoku):
    the_queue = queue.Queue()

    # creates possible values to the domains of each cell
    csp = fillDomain(sudoku)
    # csp = [[], []]
    # [0] = cell (coordinateX, coordinateY)
    # [1] = domain of possible values

    # creates a queue of arcs
    fill_arc_queue(the_queue)

    # iterates the queue of arcs
    while not the_queue.empty():
        arc = the_queue.get()

        cell1 = arc[0]
        lineX = cell1[0]
        colY = cell1[1]

        cell2 = arc[1]
        # verify if the 2nd cell is Occupied cell (a cell with different number than 0)
        # if so, then it removes that value from the domain of 1st cell (thus cell1's domain becomes thinner)
        if revise(csp, cell1, cell2):
            # checks if the domain of 1st cell is empty, if so it ends by returning a boolean False
            # (not possible to continue to resolve with ac3)
            if len(csp[1][csp[0].index(cell1)]) == 0:
                return False
            else:
                # checking others
                neighborsAux = getNeighbors(lineX, colY)
                for i in neighborsAux:
                    the_queue.put([i, cell1])
                    the_queue.put([cell1, i])

    # formatting the matrix
    k = 0
    for i in range(9):
        for j in range(9):
            # replacing 0 with the solved number
            sudoku[i][j] = csp[1][k]
            k = k + 1
    # returned the sudoku solved
    return sudoku


# Function that will format (so we call display it latter)
def divide_chunks(the_list):
    new_list = []

    # flattens a double array
    # turns each elem from it turns into a individual array
    for elem in [item for sublist in the_list for item in sublist]:
        new_list.append([elem])

    # divides the array into smaller chunks of 9
    for i in range(0, len(new_list), 9):
        yield new_list[i:i + 9]

    # returns the formatted list
    return new_list


# Function to solve sudoku and print it
def solve_sudoku(sudoku):
    # Prints the unsolved sudoku

    format_list = divide_chunks(sudoku)

    print("Original Sudoku (not solved):")
    unsolved_sudoku = pd.DataFrame(format_list)
    unsolved_sudoku.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    unsolved_sudoku.index = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # printed
    print(unsolved_sudoku, "\n")

    # calls the function with ac3 algorithm to solve it
    sudoku = ac3(sudoku)
    print("----------------------------------------------", "\n")

    # Prints the solved sudoku
    print("The Solution to Sudoku:")
    solved_sudoku = pd.DataFrame(sudoku)
    solved_sudoku.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    solved_sudoku.index = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # printed
    print(solved_sudoku)


'''---------------------------------------- Testing the Sudoku Solver ----------------------------------------'''


solve_sudoku(matrix)
