import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-3, 3, 100)

# Calculate sin and cos values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the graphs
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
