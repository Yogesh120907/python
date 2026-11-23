"""
Experiment 28: Interactive bar chart using Plotly showing marks obtained in Mathematics.
"""
import pandas as pd
import plotly.express as px

data = {
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Student",
    y="Mathematics",
    text="Mathematics",
    color="Mathematics",
    color_continuous_scale="Viridis",
    title="Interactive Bar Chart: Mathematics Marks by Student",
    labels={"Mathematics": "Mathematics Marks (out of 100)"},
)

fig.update_traces(textposition="outside")
fig.update_layout(yaxis_range=[0, 105])
fig.write_html("math_marks_interactive.html")
print("Interactive chart saved to 'math_marks_interactive.html'.")
fig.show()
