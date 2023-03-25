import java.util.Objects;

public class Particle {
    private final int id;
    private double x, y, v, theta, radius;

    public Particle(int id, double x, double y, double v, double theta, double radius) {
        this.id = id;
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.v = v;
        this.theta = theta; // angle θ of the velocity
    }

    public Particle copy() {
        return new Particle(this.id, this.x, this.y, this.v, this.theta, this.radius);
    }

    public int getId() {
        return id;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getRadius() {
        return radius;
    }

    public double getV() {
        return v;
    }

    public double getTheta() {
        return theta;
    }

    public void setTheta(double theta) { this.theta = theta; }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Particle particle = (Particle) o;
        return id == particle.id;
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
