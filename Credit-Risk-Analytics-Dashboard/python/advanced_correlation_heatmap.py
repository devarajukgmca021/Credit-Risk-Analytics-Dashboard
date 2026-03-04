"""
Credit Risk Analytics Dashboard
Visualization: Advanced Financial Correlation Heatmap

Author: Devaraju K G

Description:
This script generates a correlation heatmap to analyze the
relationships between numerical financial variables in the
credit risk dataset.

The heatmap helps identify positive and negative correlations
between variables such as:
- Annual Income
- Loan Amount
- Credit Score
- Interest Rate
- Debt-to-Income Ratio

Stronger correlations may indicate potential risk patterns
in borrower financial behavior.
"""

# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Compute correlation matrix for numerical variables
corr = dataset.corr()

# Create figure with defined size
plt.figure(figsize=(8,6))

# Generate heatmap visualization
sns.heatmap(
    corr,
    annot=True,       # Display correlation values
    cmap="coolwarm",  # Color gradient for correlation strength
    fmt=".2f"         # Format values to two decimal places
)

# Add title
plt.title("Financial Variable Correlation Matrix")

# Display the heatmap
plt.show()