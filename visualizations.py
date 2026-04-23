import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('race data/combined_output.csv')

# Create histogram with raceid on x-axis and delta on y-axis
plt.figure(figsize=(12, 6))
plt.hist(df['position_delta'], bins=10, color='steelblue', edgecolor='black')
plt.xlabel('Position Delta')
plt.ylabel('Frequency')
plt.title('Position Delta Distribution')
plt.tight_layout()
plt.savefig('position_delta_chart.png', dpi=150)
plt.close()