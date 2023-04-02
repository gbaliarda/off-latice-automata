import numpy as np
from parsers import parse_static_inputs, parse_simulation_output, parse_config, ITERATIONS

# Parse the static inputs
N, L, steps = parse_static_inputs()

# Parse the simulation output
parse_simulation_output(N, steps)

va_stationary_t = parse_config()

# Time steps to plot
t = np.arange(va_stationary_t, ITERATIONS, 1)

# v_a for each time step
v_a = np.zeros(ITERATIONS - va_stationary_t)

# Compute v_a for each time step
for i in range(va_stationary_t, ITERATIONS):
  # Sum the velocities of all particles as a vector
  V = np.array([0.0, 0.0])
  for j in range(N):
    v = steps[i][j][2]
    theta = steps[i][j][3]
    V += np.array([v * np.cos(theta), v * np.sin(theta)])
  # Compute the magnitude of the sum of the velocities
  V = np.linalg.norm(V)
  
  v_a[i - va_stationary_t] = (1 / (N*v)) * V

# Compute mean and std
mean_va = np.mean(v_a)
std_va = np.std(v_a)

print(f"Mean v_a: {mean_va}")
print(f"Std v_a: {std_va}")