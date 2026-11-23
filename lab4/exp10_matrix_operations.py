import numpy as np

def add_matrices_py(A: list[list], B: list[list]) -> list[list]:
    rows, cols = len(A), len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

def subtract_matrices_py(A: list[list], B: list[list]) -> list[list]:
    rows, cols = len(A), len(A[0])
    return [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]

def multiply_matrices_py(A: list[list], B: list[list]) -> list[list]:
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Invalid dimensions for matrix multiplication.")
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose_matrix_py(A: list[list]) -> list[list]:
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print("Py Addition:", add_matrices_py(mat1, mat2))
    print("Py Subtraction:", subtract_matrices_py(mat1, mat2))
    print("Py Multiplication:", multiply_matrices_py(mat1, mat2))
    print("Py Transpose:", transpose_matrix_py(mat1))
    np_mat1, np_mat2 = np.array(mat1), np.array(mat2)
    print("\nNumPy Addition:\n", np_mat1 + np_mat2)
    print("NumPy Multiplication:\n", np.dot(np_mat1, np_mat2))
