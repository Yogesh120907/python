import numpy as np

def analyze_academic_performance():
    subjects = ['S1', 'S2', 'S3', 'S4', 'S5']
    mid_sem = np.array([
        [65, 70, 68, 72],
        [78, 75, 80, 77],
        [55, 60, 58, 62],
        [82, 85, 80, 88],
        [70, 68, 72, 74]
    ])
    end_sem = np.array([
        [72, 78, 75, 80],
        [84, 82, 86, 83],
        [65, 68, 66, 70],
        [88, 90, 85, 92],
        [78, 75, 80, 82]
    ])

    mid_avg = np.mean(mid_sem, axis=1)
    end_avg = np.mean(end_sem, axis=1)
    pct_improvement = ((end_avg - mid_avg) / mid_avg) * 100

    for i, subj in enumerate(subjects):
        print(f"Subject {subj}:")
        print(f"  Mid-Sem Avg: {mid_avg[i]:.2f} | End-Sem Avg: {end_avg[i]:.2f}")
        print(f"  Improvement: {pct_improvement[i]:.2f}%\n")

if __name__ == "__main__":
    analyze_academic_performance()
