import numpy as np
import matplotlib.pyplot as plt
from parsers import ITERATIONS

# JUMP TO LINE 67 TO SEE THE MAIN FUNCTION

def compute_va_time(N: int, t_0: int, steps: dict[int, dict[int, list[float]]]):
  # v_a for each time step
  v_a = np.zeros(ITERATIONS)

  # Compute v_a for each time step
  for i in range(t_0, ITERATIONS):
    # Sum the velocities of all particles as a vector
    V = np.array([0.0, 0.0])
    for j in range(N):
      v = steps[i][j][2]
      theta = steps[i][j][3]
      V += np.array([v * np.cos(theta), v * np.sin(theta)])
    # Compute the magnitude of the sum of the velocities
    V = np.linalg.norm(V)
    
    v_a[i] = (1 / (N*v)) * V

  return v_a


def parse_simulation_output(N, steps: dict[int, dict[int, list[float]]], file_path: str):
  with open(file_path, "r") as f:
    particle_counter = 0
    t = 0
    skip_line = True

    for line in f:
      # skip the time indicator line
      if particle_counter % N == 0 and skip_line == True:
        t += 1
        steps[t] = {} # create a new time step
        skip_line = False
        continue

      properties = [float(x) for x in line.rstrip("\n").split(" ")]
      steps[t][properties[0]] = [x for x in properties[1:]]

      particle_counter += 1
      skip_line = True

    return steps

# Time steps to plot
t = np.arange(0, ITERATIONS, 1)

# Amount of experiments to run
EXPERIMENTS = 2

# List of experiments to run
parameters = {
  "output_files": ["output_400_10.txt", "output_100_5.txt"],
  "N": [400, 100],
  "labels": ["N=400, L=10, η=1", "N=100, L=5, η=1"]
}

# Save the particles positions, velocity and angle at each time step
steps: dict[int, dict[int, list[float]]] = {}

for i in range(EXPERIMENTS):
  N = parameters["N"][i]

  # Parse the simulation output
  parse_simulation_output(N, steps, parameters["output_files"][i])

  # Compute v_a for each time step
  v_a = compute_va_time(N, 1, steps)

  plt.plot(t, v_a, label=parameters["labels"][i])

plt.xlabel('tiempo', fontsize=20)
plt.ylabel('vₐ', fontsize=20)

plt.legend()
plt.grid()
plt.show()
