import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# -------------------------
# 1. Setup Seaborn Styling
# -------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready text scaling

# -------------------------
# 2. Generate Synthetic Customer Data
# -------------------------
np.random.seed(42)

segments = ["Budget", "Mid-Tier", "Premium", "VIP"]

data = pd.DataFrame({
    "Customer_Segment": np.repeat(segments, 200),
    "Purchase_Amount": np.concatenate([
        np.random.normal(40, 10, 200),   # Budget segment
        np.random.normal(120, 30, 200),  # Mid-Tier
        np.random.normal(350, 70, 200),  # Premium
        np.random.normal(800, 150, 200)  # VIP
    ])
})

# Ensure values are realistic (no negative spending)
data["Purchase_Amount"] = data["Purchase_Amount"].clip(lower=5)

# -------------------------
# 3. Create Boxplot
# -------------------------
plt.figure(figsize=(8, 8), dpi=64)  # EXACTLY 512px output

sns.boxplot(
    data=data,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="viridis"
)

# -------------------------
# 4. Labels and Title
# -------------------------
plt.title("Purchase Amount Distribution by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")
plt.xticks(rotation=15)

# -------------------------
# 5. Save EXACT SIZE IMAGE
# -------------------------
plt.savefig("chart.png", dpi=64)  # No bbox_inches — required for exact pixels
plt.close()
