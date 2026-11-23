from scipy.optimize import minimize

def cost_function(x: float) -> float:
    return x**2 + 54 / x

def optimize_function():
    initial_guess = 2.0
    result = minimize(cost_function, initial_guess, bounds=[(0.1, None)])
    return result

if __name__ == "__main__":
    res = optimize_function()
    print(f"Optimization Success: {res.success}")
    print(f"Optimal x: {res.x[0]:.4f}")
    print(f"Minimum function value: {res.fun:.4f}")
