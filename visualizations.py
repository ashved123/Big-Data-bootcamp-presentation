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

# --- Constructor Championship Points vs Average Qualifying Position ---
constructor_standings = pd.read_csv('race data/constructor_standings.csv')
constructor_points = constructor_standings.groupby('constructorId')['points'].sum().reset_index()
constructor_points.columns = ['constructorId', 'total_points']

qualifying = pd.read_csv('race data/qualifying.csv')
avg_qualifying = qualifying.groupby('constructorId')['position'].mean().reset_index()
avg_qualifying.columns = ['constructorId', 'avg_qualifying_position']

comparison = pd.merge(constructor_points, avg_qualifying, on='constructorId', how='inner')
comparison = comparison.sort_values('total_points', ascending=False)

# Create grouped bar chart
fig, ax1 = plt.subplots(figsize=(14, 8))

x = range(len(comparison))
bar_width = 0.35

# Bar chart for constructor points
bars1 = ax1.bar([i - bar_width/2 for i in x], comparison['total_points'], bar_width, 
                label='Total Points', color='steelblue', alpha=0.8)
ax1.set_xlabel('Constructor', fontsize=14)
ax1.set_ylabel('Total Championship Points', fontsize=14, color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')

# Second y-axis for average qualifying position
ax2 = ax1.twinx()
bars2 = ax2.bar([i + bar_width/2 for i in x], comparison['avg_qualifying_position'], bar_width, 
                label='Avg Qualifying Position', color='orange', alpha=0.8)
ax2.set_ylabel('Average Qualifying Position', fontsize=14, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
ax2.invert_yaxis()  # Lower position is better, so invert


# Add constructor labels, offsetting every other label vertically to avoid overlap
labels = [f'C{int(c)}' for c in comparison['constructorId']]
tick_positions = list(x)
ax1.set_xticks(tick_positions)
ax1.set_xticklabels([''] * len(labels))  # Remove default labels

# Draw custom labels with vertical offset
for i, (tick, label) in enumerate(zip(tick_positions, labels)):
    y_offset = -30 if i % 2 == 0 else -50
    ax1.annotate(label, xy=(tick, 0), xytext=(0, y_offset), textcoords='offset points',
                ha='center', va='top', fontsize=12, rotation=30)

# Add legend above the plot
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', bbox_to_anchor=(0.5, 1.10), ncol=2, fontsize=12, frameon=False)

plt.title('Constructor Championship Points vs Average Qualifying Position', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('constructor_qualifying_scatter.png', dpi=150)
plt.close()