"""
Credit Risk Analytics Dashboard
Visualization: Loan Purpose Relationship Network

Author: Devaraju K G

Description:
This script generates a network graph to visualize the relationship
between Regions and Loan Purposes in the credit risk dataset.

Each node represents either a region or a loan purpose, and edges
connect them based on occurrences in the dataset.

This visualization helps understand which loan purposes are most
common in specific regions and highlights structural relationships
within the loan portfolio.
"""

# Import required libraries
import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add edges between Region and Loan Purpose
for i in range(len(dataset)):
    G.add_edge(
        dataset.iloc[i]["Region"],       # Region node
        dataset.iloc[i]["Loan_Purpose"]  # Loan purpose node
    )

# Set figure size
plt.figure(figsize=(10,8))

# Generate layout for node positions
pos = nx.spring_layout(G, seed=42)

# Draw the network graph
nx.draw(
    G,
    pos,
    with_labels=True,   # Display node labels
    node_size=3000,     # Size of nodes
    node_color="skyblue",
    font_size=10
)

# Add title
plt.title("Regional Loan Purpose Relationship Network")

# Display the graph
plt.show()