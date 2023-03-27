# function to add two matrices
def add_matrices(mat1, mat2):
    # get dimensions of the matrices
    rows = len(mat1)
    cols = len(mat1[0])
    # initialize a result matrix with zeros
    result = [[0 for j in range(cols)] for i in range(rows)]
    # iterate over each element of the matrices and add them
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

# take input from user for matrix 1
rows = int(input("Enter the number of rows for matrix 1: "))
cols = int(input("Enter the number of columns for matrix 1: "))
mat1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input("Enter the element at position ({}, {}): ".format(i, j)))
        row.append(val)
    mat1.append(row)

# take input from user for matrix 2
rows = int(input("Enter the number of rows for matrix 2: "))
cols = int(input("Enter the number of columns for matrix 2: "))
mat2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input("Enter the element at position ({}, {}): ".format(i, j)))
        row.append(val)
    mat2.append(row)

# check if the matrices can be added
if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
    # add the matrices
    result = add_matrices(mat1, mat2)
    # display the result
    print("Matrix 1:", mat1)
    print("Matrix 2:", mat2)
    print("Sum of matrices:", result)
else:
    print("Matrices cannot be added because their dimensions are different.")
