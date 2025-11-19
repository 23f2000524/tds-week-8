import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# -------------------------
# 1. Setup Seaborn Styling
# -------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready typography

# -------------------------
# 2. Generate Synthetic Customer Data
# -------------------------
np.random.seed(42)

segments = ["Budget", "Mid-Tier", "Premium", "VIP"]

data = pd.DataFrame({
    "Customer_Segment": np.repeat(segments, 200),
    "Purchase_Amount": np.concatenate([
        np.random.normal(40, 10, 200),   # Budget
        np.random.normal(120, 30, 200),  # Mid-Tier
        np.random.normal(350, 70, 200),  # Premium
        np.random.normal(800, 150, 200)  # VIP
    ])
})

# Ensure no negative values (realistic constraint)
data["Purchase_Amount"] = data["Purchase_Amount"].clip(lower=5)

# -------------------------
# 3. Create Boxplot
# -------------------------
plt.figure(figsize=(8, 8))  # Required for 512 x 512 px at DPI=64

sns.boxplot(
    data=data,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="viridis"
)

# -------------------------
# 4. Chart Labels and Title
# -------------------------
plt.title("Purchase Amount Distribution by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")
plt.xticks(rotation=15)

# -------------------------
# 5. Export Image
# -------------------------
# 8×8 inches at 64 DPI = 512×512 pixels
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("chart.png successfully generated in root directory.")
