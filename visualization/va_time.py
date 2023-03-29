import numpy as np
import matplotlib.pyplot as plt
from parsers import parse_static_inputs, parse_simulation_output, ITERATIONS

# Parse the static inputs
N, L, steps = parse_static_inputs()

# Parse the simulation output
parse_simulation_output(N, steps)

# Time steps to plot
t = np.arange(0, ITERATIONS, 1)

# v_a for each time step
v_a = np.zeros(ITERATIONS)

# Compute v_a for each time step
for i in range(ITERATIONS):
  # Sum the velocities of all particles as a vector
  V = np.array([0.0, 0.0])
  for j in range(N):
    v = steps[i][j][2]
    theta = steps[i][j][3]
    V += np.array([v * np.cos(theta), v * np.sin(theta)])
  # Compute the magnitude of the sum of the velocities
  V = np.linalg.norm(V)
  
  v_a[i] = (1 / (N*v)) * V

# Plot v_a vs. time
plt.plot(t, v_a)
plt.xlabel('t')
plt.ylabel('v_a')
plt.title('v_a vs. time')
plt.grid()
plt.show()