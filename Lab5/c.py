# Get the number of rows and columns for the first matrix from the user
num_rows1 = int(input("Enter the number of rows for the first matrix: "))
num_cols1 = int(input("Enter the number of columns for the first matrix: "))

# Initialize the first matrix with zeros
matrix1 = []
for i in range(num_rows1):
    row = []
    for j in range(num_cols1):
        row.append(0)
    matrix1.append(row)

# Get the values for the first matrix from the user
for i in range(num_rows1):
    for j in range(num_cols1):
        matrix1[i][j] = int(input(f"Enter the value for element ({i+1}, {j+1}) in the first matrix: "))

# Get the number of rows and columns for the second matrix from the user
num_rows2 = int(input("Enter the number of rows for the second matrix: "))
num_cols2 = int(input("Enter the number of columns for the second matrix: "))

# Initialize the second matrix with zeros
matrix2 = []
for i in range(num_rows2):
    row = []
    for j in range(num_cols2):
        row.append(0)
    matrix2.append(row)

# Get the values for the second matrix from the user
for i in range(num_rows2):
    for j in range(num_cols2):
        matrix2[i][j] = int(input(f"Enter the value for element ({i+1}, {j+1}) in the second matrix: "))

# Check if the matrices can be multiplied
if num_cols1 != num_rows2:
    print("Error: Number of columns in first matrix should be equal to number of rows in second matrix")
else:
    # Initialize the result matrix with zeros
    result_matrix = []
    for i in range(num_rows1):
        row = []
        for j in range(num_cols2):
            row.append(0)
        result_matrix.append(row)

    # Multiply the matrices
    for i in range(num_rows1):
        for j in range(num_cols2):
            for k in range(num_cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    # Print the result matrix
    print("Result Matrix:")
    for row in result_matrix:
        print(row)
