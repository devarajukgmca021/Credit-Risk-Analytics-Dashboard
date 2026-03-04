"""
Credit Risk Analytics Dashboard
Visualization: Financial Correlation Heatmap

Author: Devaraju K G

Description:
This script generates a correlation heatmap to analyze the
relationships between key financial variables in the banking
credit risk dataset. It helps identify positive or negative
correlations between variables such as income, loan amount,
credit score, interest rate, and debt-to-income ratio.
"""

# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate correlation matrix from the dataset
corr = dataset.corr()

# Create the heatmap visualization
sns.heatmap(
    corr,
    annot=True,        # Shows correlation values inside cells
    cmap="coolwarm"    # Color scheme for positive/negative correlation
)

# Add chart title
plt.title("Financial Variable Correlation Matrix")

# Display the heatmap
plt.show()