# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, name="matrix"):
    print(f"Enter {name}:")
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        row = [int(x) for x in row]
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        print(" ".join(str(val) for val in row))


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(matrix_a[r][c] + matrix_b[r][c])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for r in range(rows_a):
        new_row = []
        for c in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[r][k] * matrix_b[k][c]
            new_row.append(total)
        result.append(new_row)
    return result


# PART A - Transpose
print("PART A: Transpose a Matrix")
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
matrix = read_matrix(m, n)
print("\nOriginal Matrix:")
display_matrix(matrix)
print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))

# PART B - Add
print("\nPART B: Add Two Matrices")
m2 = int(input("Enter number of rows: "))
n2 = int(input("Enter number of columns: "))
matrix_a = read_matrix(m2, n2, "Matrix A")
matrix_b = read_matrix(m2, n2, "Matrix B")
print("\nSum:")
display_matrix(add_matrices(matrix_a, matrix_b))

# PART C - Multiply
print("\nPART C: Multiply Two Matrices")
m3 = int(input("Enter rows for Matrix A: "))
n3 = int(input("Enter columns for Matrix A (rows for Matrix B): "))
p3 = int(input("Enter columns for Matrix B: "))
matrix_a2 = read_matrix(m3, n3, "Matrix A")
matrix_b2 = read_matrix(n3, p3, "Matrix B")
print("\nProduct:")
display_matrix(multiply_matrices(matrix_a2, matrix_b2))