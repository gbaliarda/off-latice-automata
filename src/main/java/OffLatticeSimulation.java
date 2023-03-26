import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class OffLatticeSimulation {
    private List<Particle> particles;
    private final int L;
    private final double eta, dt;
    private int t; // current time

    public OffLatticeSimulation(Input input, double eta) {
        this.particles = input.getParticles();
        this.L = input.getL();
        this.t = 0;
        this.eta = eta;
        this.dt = 1; // time unit
    }

    public void nextState() {
        CellIndexMethod cim = new CellIndexMethod(particles, L, true);
        Map<Particle, List<Particle>> neighbourhoods = cim.computeNeighbourhoods();
        particles.forEach(particle -> {
            // Update particle theta
            List<Particle> neighbours = neighbourhoods.getOrDefault(particle, new LinkedList<>());
            double newTheta = computeNewTheta(particle, neighbours);
            particle.setTheta(newTheta);

            // Update particle position
            Position newPosition = computeNewPosition(particle);
            particle.setX(newPosition.getX());
            particle.setY(newPosition.getY());
        });
        // Update time
        t += dt;
    }

    private double computeNewTheta(Particle particle, List<Particle> neighbours) {
        // Angles of the particle and all its neighbours
        List<Double> angles = neighbours.stream().map(Particle::getTheta).collect(Collectors.toList());
        angles.add(particle.getTheta());

        double avgSin = angles.stream().mapToDouble(Math::sin).average().orElse(0.0);
        double avgCos = angles.stream().mapToDouble(Math::cos).average().orElse(0.0);

        return Math.atan2(avgSin, avgCos) + Math.random()*eta - eta/2;
    }

    private Position computeNewPosition(Particle particle) {
        double vx = particle.getV() * Math.cos(particle.getTheta());
        double vy = particle.getV() * Math.sin(particle.getTheta());
        double newX = (particle.getX() + vx * dt) % this.L;
        double newY = (particle.getY() + vy * dt) % this.L;
        if (newX < 0)
            newX += 25;
        if (newY < 0)
            newY += 25;
        return new Position(newX, newY);
    }

    public List<Particle> getParticles() {
        return particles;
    }

    public int getTime() {
        return t;
    }

    private static class Position {
        double x;
        double y;

        public Position(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double getX() {
            return x;
        }

        public double getY() {
            return y;
        }
    }
}
