"""
Credit Risk Analytics Dashboard
Visualization: Credit Score Violin Distribution

Author: Devaraju K G

Description:
This script generates a violin plot to visualize the distribution
of credit scores for different loan statuses (Approved vs Default).
The violin plot helps understand how credit score patterns vary
between borrowers whose loans were approved and those who defaulted.

The shape of the violin shows the density of credit scores,
allowing deeper insight into borrower risk distribution.
"""

# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Set figure size for better visualization
plt.figure(figsize=(8,6))

# Create violin plot
sns.violinplot(
    x=dataset["Loan_Status"],      # Loan status categories
    y=dataset["Credit_Score"],     # Credit score distribution
    palette={
        "Approved": "#2ECC71",     # Green for approved loans
        "Default": "#D7263D"       # Red for defaulted loans
    }
)

# Add titles and labels
plt.title("Credit Score Distribution by Loan Status")
plt.xlabel("Loan Status")
plt.ylabel("Credit Score")

# Display the plot
plt.show()