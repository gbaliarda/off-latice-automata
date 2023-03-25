import numpy as np
import tomllib

# Configuration
with open("config.toml", "rb") as f:
  config = tomllib.load(f)
  STATIC_FILE = config["files"]["static_input"]
  N = config["simulation"]["N"]
  L = config["simulation"]["L"]

PARTICLE_RADIUS = 0.00
INTERACTION_RADIUS = 1.0
VELOCITY = 0.03

def generate_static_file():
    with open(STATIC_FILE, "w") as f:
        f.write(f"{N}\n")
        f.write(f"{L}\n")
        f.write(f"{INTERACTION_RADIUS}\n")

        for i in range(0, N):
            random_numbers = np.random.rand(3)
            x = random_numbers[0] * L
            y = random_numbers[1] * L
            theta = random_numbers[2]*2*np.pi - np.pi # radians
            f.write(f"{PARTICLE_RADIUS} {x} {y} {VELOCITY} {theta}\n")

if __name__ == "__main__":
    generate_static_file()