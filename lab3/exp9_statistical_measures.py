import math
import numpy as np

def compute_pure_python_stats(data: list[float]) -> dict:
    n = len(data)
    mean_val = sum(data) / n
    sorted_data = sorted(data)
    if n % 2 == 0:
        median_val = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median_val = sorted_data[n // 2]
    variance = sum((x - mean_val) ** 2 for x in data) / n
    std_val = math.sqrt(variance)
    return {
        "mean": mean_val,
        "median": median_val,
        "std": std_val,
        "min": sorted_data[0],
        "max": sorted_data[-1]
    }

def compute_numpy_stats(data: list[float]) -> dict:
    arr = np.array(data)
    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr))
    }

if __name__ == "__main__":
    datasets = {
        "marks": [78, 85, 92, 67, 88, 73, 95, 81, 76, 89],
        "temperatures": [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5],
        "sales": [12500, 13800, 14200, 11900, 15100, 14750, 16000]
    }
    for name, data in datasets.items():
        print(f"--- Dataset: {name} ---")
        print("Pure Python:", compute_pure_python_stats(data))
        print("NumPy:      ", compute_numpy_stats(data))
        print()
