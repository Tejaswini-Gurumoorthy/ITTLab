# Get the number of rows and columns for the matrix from the user
num_rows = int(input("Enter the number of rows in the matrix: "))
num_cols = int(input("Enter the number of columns in the matrix: "))

# Initialize the matrix with zeros
matrix = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        row.append(0)
    matrix.append(row)

# Get the values for the matrix from the user
for i in range(num_rows):
    for j in range(num_cols):
        matrix[i][j] = int(input(f"Enter the value for element ({i+1}, {j+1}): "))

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Calculate the transpose of the matrix
transpose_matrix = []
for j in range(num_cols):
    row = []
    for i in range(num_rows):
        row.append(matrix[i][j])
    transpose_matrix.append(row)

# Print the transpose of the matrix
print("Transpose Matrix:")
for row in transpose_matrix:
    print(row)
