import math

def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

if __name__ == "__main__":
    test_number = 7
    print(f"Factorial of {test_number}: {calculate_factorial(test_number)}")
    print(f"Is {test_number} prime? {is_prime(test_number)}")
