import matplotlib.pyplot as plt
import numpy as np

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 3))

# Example 1: Points of the set {1/n}
n_values = np.arange(1, 21)
points = 1 / n_values

# Plot the points {1/n}
ax.plot(points, np.zeros_like(points), 'bo', label=r'Points of $\{1/n\}$')

# Highlight the limit point 0
ax.plot(0, 0, 'ro', label='Limit point (0)')

# Decorations
ax.set_ylim(-0.1, 0.1)
ax.set_xlim(-0.1, 1.1)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='red', linestyle='--', linewidth=1)

# Labels
ax.set_xlabel('Real Line')
ax.set_yticks([])
ax.set_title('Visualization of Limit Point Example')

# Legend
ax.legend(loc='upper right')

# Show the plot
plt.show()
