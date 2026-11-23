def fibonacci_recursive(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def generate_fibonacci_series(terms: int) -> list[int]:
    if terms <= 0:
        return []
    return [fibonacci_recursive(i) for i in range(terms)]

if __name__ == "__main__":
    n_terms = 10
    series = generate_fibonacci_series(n_terms)
    print(f"Fibonacci series ({n_terms} terms): {series}")
