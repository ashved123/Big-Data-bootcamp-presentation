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

comparison = pd.read_csv('race data/lap_time_comparison.csv')

# Histogram: time delta (race - qualifying) on x-axis, frequency on y-axis
plt.figure(figsize=(12, 6))

# Calculate time delta in seconds
comparison['delta_seconds'] = comparison['diff_ms'] / 1000

# Determine bin step - use 0.5 second bins for reasonable visualization
bin_step = 0.5
min_delta = comparison['delta_seconds'].min()
max_delta = comparison['delta_seconds'].max()
bins = int((max_delta - min_delta) / bin_step) + 1

plt.hist(comparison['delta_seconds'], bins=bins, color='steelblue', edgecolor='black')
plt.xlabel('Time Delta (seconds)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Time Difference: Race Lap vs Qualifying Lap', fontsize=15)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('lap_time_comparison.png', dpi=150)
plt.close()