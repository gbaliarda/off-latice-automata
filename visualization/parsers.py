import tomllib

with open("config.toml", "rb") as f:
  config = tomllib.load(f)
  STATIC_FILE = config["files"]["static_input"]
  OUTPUT_FILE = config["files"]["output"]
  ITERATIONS = config["simulation"]["iterations"]
  N = config["simulation"]["N"]
  L = config["simulation"]["L"]

# Parse simulation settings and particles initial positions, velocity and angle
def parse_static_inputs():
  # Save the particles positions, velocity and angle at each time step
  steps: dict[int, dict[int, list[float]]] = {}
  steps[0] = {}

  with open(STATIC_FILE, "r") as f:
    # N = int(f.readline().rstrip("\n"))
    # L = float(f.readline().rstrip("\n"))
    f.readline().rstrip("\n") # skip the interaction radius line

    index = 0
    # Parse initial particle positions, velocity and angle
    for line in f:
      # skip the particle radius
      steps[0][index] = [float(x) for x in line.rstrip("\n").split(" ")][1:]
      index += 1
    
    return N, L, steps


# Parse particles positions, velocity and angles at each time step
def parse_simulation_output(N, steps):
  with open(OUTPUT_FILE, "r") as f:
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


# Check if this file is being run as a script
if __name__ == "__main__":
  # Parse the static inputs
  N, L, steps = parse_static_inputs()

  # Parse the simulation output
  parse_simulation_output(N, steps)

  print("First particle on t=0:", steps[0][0])
  print("Last particle on t=0:", steps[0][N-1])

  print("First particle on t=1:", steps[1][0])
  print("Last particle on t=1:", steps[1][N-1])

  print("First particle on t=2:", steps[2][0])
  print("Last particle on t=2:", steps[2][N-1])
