import numpy as np

def compute_matrix_properties(matrix: np.ndarray) -> tuple[float, np.ndarray, int]:
    det = np.linalg.det(matrix)
    inv = None if np.isclose(det, 0) else np.linalg.inv(matrix)
    rank = np.linalg.matrix_rank(matrix)
    return det, inv, rank

if __name__ == "__main__":
    A = np.array([[2, 1, 3],
                  [1, 0, 2],
                  [4, 1, 8]], dtype=float)
    det_A, inv_A, rank_A = compute_matrix_properties(A)
    print(f"Determinant:\n{det_A:.4f}\n")
    print(f"Inverse:\n{inv_A}\n")
    print(f"Rank:\n{rank_A}")
