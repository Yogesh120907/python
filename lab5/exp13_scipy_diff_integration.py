import numpy as np
from scipy.integrate import quad

def target_function(x: float) -> float:
    return np.sin(x) + x**2

def numerical_derivative(func, x: float, h: float = 1e-6) -> float:
    return (func(x + h) - func(x - h)) / (2 * h)

def perform_integration(func, a: float, b: float) -> tuple[float, float]:
    integral_val, abs_error = quad(func, a, b)
    return integral_val, abs_error

if __name__ == "__main__":
    x_eval = np.pi / 4
    deriv = numerical_derivative(target_function, x_eval)
    integral, error = perform_integration(target_function, 0, np.pi)
    print(f"Derivative at x = pi/4: {deriv:.6f}")
    print(f"Definite Integral from 0 to pi: {integral:.6f} (Error: {error:.2e})")
