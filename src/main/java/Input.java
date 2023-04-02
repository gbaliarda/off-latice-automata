import java.util.List;

public class Input {
    private long amountParticles;
    private double interactionRadius, L;
    private List<Particle> particles;

    public void setParticles(List<Particle> particles) {
        this.particles = particles;
    }

    public Input() {}

    public long getAmountParticles() {
        return amountParticles;
    }

    public double getL() {
        return L;
    }

    public double getInteractionRadius() {
        return interactionRadius;
    }

    public List<Particle> getParticles() {
        return particles;
    }

    public void setAmountParticles(long amountParticles) {
        this.amountParticles = amountParticles;
    }

    public void setL(double L) {
        this.L = L;
    }

    public void setInteractionRadius(double interactionRadius) {
        this.interactionRadius = interactionRadius;
    }

    public List<Particle> addParticle(Particle particle) {
        particles.add(particle);
        return particles;
    }
}
