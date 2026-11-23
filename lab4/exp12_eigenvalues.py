import numpy as np

def compute_eigen_components(matrix: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

if __name__ == "__main__":
    A = np.array([[4, -2],
                  [1,  1]], dtype=float)
    values, vectors = compute_eigen_components(A)
    print("Eigenvalues:", values)
    print("\nEigenvectors (column-wise):\n", vectors)
