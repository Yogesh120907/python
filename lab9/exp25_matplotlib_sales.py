"""
Experiment 25: Visualize monthly retail sales revenue using line & bar charts
and identify the highest and lowest sales months.
"""
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [45000, 52000, 48000, 61000, 58000, 65000, 62000, 70000, 68000, 75000, 72000, 80000]

max_sales = max(sales)
min_sales = min(sales)
max_month = months[sales.index(max_sales)]
min_month = months[sales.index(min_sales)]

print(f"Highest Sales: {max_month} (₹{max_sales:,})")
print(f"Lowest Sales : {min_month} (₹{min_sales:,})")

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

axes[0].plot(months, sales, marker="o", color="#1f77b4", linewidth=2)
axes[0].set_title("Monthly Retail Sales Trend (Line Chart)")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales (₹)")
axes[0].grid(True, linestyle="--", alpha=0.5)

colors = ["#2ca02c" if s == max_sales else "#d62728" if s == min_sales else "#4c78a8" for s in sales]
axes[1].bar(months, sales, color=colors)
axes[1].set_title("Monthly Retail Sales Comparison (Bar Chart)")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Sales (₹)")

plt.tight_layout()
plt.savefig("monthly_sales_charts.png", dpi=150)
plt.show()
