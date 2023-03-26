# Requirements

- python >= 3.10
  - numpy
  - matplotlib
- java >= 11

# Input Generation

In order to generate random input particles run the following command:

```shell
python generate_particles.py
```

The structure of `static.txt` is:

```
N
L
interaction_radius
radius_1 pos_x1 pos_y1 vel_1 theta_1
...
radius_N pos_xN pos_yN vel_N theta_N
```

# Configuration

Project configuration can be changed modifying the `config.toml` file:

```toml
[simulation]
L = 25              # board size
N = 300             # amount of particles
eta = 0.1           # noise
iterations = 1000   # time steps on the simulation

[files]
static_input = "./static.txt"
output = "./output.txt"
```

# Run Simulation

To generate the .jar file run the following command:

```shell  
mvn clean package
```

In order to run the simulation run:

```shell
java -jar ./target/off-latice-automata-1.0-SNAPSHOT-jar-with-dependencies.jar
```

This will generate a file called output.txt.

The structure of `output.txt` is:

```
iteration
particle_id_1 pos_x1 pos_y1 vel_1 theta_1
...
particle_id_N pos_xN pos_yN vel_N theta_N
```

# Run Animation

To run the animations based on the simulation output, execute from the root folder:

```shell
python visualization/visuals.py
```

# Authors

- Baliarda Gonzalo - 61490
- Pérez Ezequiel - 61475
