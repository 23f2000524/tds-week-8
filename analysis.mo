# email: 23f2000524@ds.study.iitm.ac.in
# This notebook demonstrates variable dependencies, interactivity,
# and dynamic documentation using Marimo.

import marimo as mo
import numpy as np
import pandas as pd
import plotly.express as px

# Cell 1: Create data
# Data flows to visualization and markdown cells below

np.random.seed(42)
x = np.linspace(0, 10, 100)
noise = np.random.normal(0, 1, 100)

df = pd.DataFrame({
    "x": x,
    "y": 2 * x + noise
})

df.head()

# Cell 2: Create an interactive slider (widget)
# This widget value dynamically affects plot and markdown content

slope = mo.ui.slider(start=1, stop=5, value=2, step=0.1, label="Adjust Model Slope")

slope

# Cell 3: Dependent calculation based on slider value
# Updating slope affects predicted values and visualizations

df["predicted"] = slope.value * df["x"]

df

# Cell 4: Visualization (depends on updated dataframe)

fig = px.line(df, x="x", y=["y", "predicted"], title="Actual vs. Adjusted Model Prediction")
fig

# Cell 5: Dynamic Markdown output based on slider state

mo.md(f"""
### 📌 Model Summary

You selected a slope of **`{slope.value}`**.

- The dataset simulates a linear relationship: `y = 2x + noise`
- The prediction line is dynamically computed: **`y = {slope.value}x`**
- Modify the slider above to observe how model assumptions affect interpretation.

""")

