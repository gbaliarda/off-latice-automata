import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

from parsers import parse_static_inputs, parse_simulation_output, ITERATIONS

# Parse the static inputs
N, L, steps = parse_static_inputs()

# Parse the simulation output
parse_simulation_output(N, steps)

# Define a function to update the position and angle of the particles
def update_particles(i):
  x_positions = [steps[i][x][0] for x in range(N)]
  y_positions = [steps[i][x][1] for x in range(N)]

  angles = [steps[i][x][3] for x in range(N)]

  x_velocities = [steps[i][x][2] * math.cos(angles[x]) for x in range(N)]
  y_velocities = [steps[i][x][2] * math.sin(angles[x]) for x in range(N)]
  
  # Clear the current plot
  plt.clf()
  plt.gcf().text(0.02, 0.95, "Iteracion: {}".format(math.floor(i / 10) * 10))
  # Plot the particles as arrows with colors based on their angles
  plt.quiver(x_positions, y_positions, x_velocities, y_velocities, angles, cmap='hsv')
  
  # Set the plot limits
  plt.xlim(0, L)
  plt.ylim(0, L)


# Create the animation using the update_particles function and a 50 millisecond interval between frames
ani = animation.FuncAnimation(plt.gcf(), update_particles, interval=30, frames=ITERATIONS, repeat=False)
ani.save("media/animation.gif")

# Display the animation
# plt.show()
