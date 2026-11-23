import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c

def fit_curve():
    x_data = np.array([1, 2, 3, 4, 5, 6], dtype=float)
    y_data = np.array([6, 17, 34, 57, 86, 121], dtype=float)
    params, _ = curve_fit(quadratic_model, x_data, y_data)
    x_dense = np.linspace(1, 6, 100)
    y_dense = quadratic_model(x_dense, *params)
    plt.scatter(x_data, y_data, color='red', label='Data Points')
    plt.plot(x_dense, y_dense, color='blue', label=f'Fit: {params[0]:.2f}x² + {params[1]:.2f}x + {params[2]:.2f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Quadratic Curve Fitting')
    plt.grid(True)
    plt.savefig('curve_fit_plot.png')
    return params

if __name__ == "__main__":
    coefficients = fit_curve()
    print(f"Fitted Parameters (a, b, c): {coefficients}")
