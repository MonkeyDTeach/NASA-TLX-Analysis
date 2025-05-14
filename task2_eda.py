# task2_eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load merged dataset
df = pd.read_csv('mergedNasatlx.csv')

# Basic stats
print("===== Basic Dataset Summary =====")
print(f"Total rows: {len(df)}")
print(f"\nMissing values per column:\n{df.isnull().sum()}")
print("\n===== Numeric Columns Summary =====")
print(df.describe())

# Most common group in each dataset type
print("\n===== Most Common Groups =====")
print("Assistant dataset:", df[df['dataset_type'] == 'assistant']['group'].mode()[0])
print("Current dataset:", df[df['dataset_type'] == 'current']['group'].mode()[0])

# Visualization 1: Mental Demand Comparison (Box Plot)
plt.figure(figsize=(12, 6))
sns.boxplot(x='group', y='mental_demand', hue='dataset_type', data=df)
plt.title("Mental Demand by Group (Assistant vs Current)")
plt.savefig('mental_demand_comparison.png')  # Save plot
plt.show()

# Visualization 2: Frustration Distribution (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(df['frustration'], bins=15, kde=True, color='purple')
plt.title("Frustration Score Distribution")
plt.xlabel("Frustration Score (0-20)")
plt.savefig('frustration_distribution.png')
plt.show()

# Visualization 3: Correlation Heatmap
numeric_cols = ['mental_demand', 'physical_demand', 'temporal_demand', 'performance', 'effort', 'frustration']
plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between NASA-TLX Dimensions")
plt.savefig('correlation_heatmap.png')
plt.show()

# Visualization 4: Interactive Scatter Plot (Plotly)
fig = px.scatter(
    df,
    x='mental_demand',
    y='frustration',
    color='group',
    facet_col='dataset_type',
    title='Mental Demand vs Frustration (Assistant vs Current)',
    labels={'mental_demand': 'Mental Demand (0-20)', 'frustration': 'Frustration (0-20)'}
)
fig.write_html('interactive_scatter.html')
fig.show()