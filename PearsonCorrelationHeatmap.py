import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Add your csv file pathe here
csv_path = r"C:\Users\Nirjon\OneDrive\ドキュメント\ArcGIS\Packages\reclassed_948cdd\commondata\pearson_correlation_matrix.csv"

df_corr = pd.read_csv(csv_path, index_col=0)

# 2. Heatmap Plotting Setup
plt.figure(figsize=(10, 8))

# 3. Heatmap Generate
sns.heatmap(
    df_corr, 
    annot=True,            # Value in each cell
    fmt=".2f",             # 2 number after point
    cmap="coolwarm",        # Color scheme (Red = Positive, Blue = Negative)
    vmin=-1, vmax=1,       # Pearson range (-1.0 to +1.0)
    linewidths=0.5,        # Grid line spacing
    cbar_kws={'label': 'Pearson Correlation Coefficient'}
)

# 4. Title & Label Formatting
plt.title("Pearson Correlation Matrix Heatmap of Flood Factors", fontsize=14, fontweight="bold", pad=15)
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.yticks(rotation=0, fontsize=10)

plt.tight_layout()

# 5. Generate Heatmap Image 
output_image = "pearson_heatmap.png"
plt.savefig(output_image, dpi=300)
plt.show()

print(f"Heatmap image successfully saved as: {output_image}")
