import com.moandjiezana.toml.Toml;

import java.io.*;
import java.util.List;

public class App {
    private static final String NO_VALUE_FOUND = "NO_VALUE_FOUND";
    private static final String OUTPUT_FILE = "output.txt";

    public static void main( String[] args ) {
        String staticFile, outputFile;
        double eta;
        try {
            // Configuration
            InputStream inputStream = new FileInputStream("config.toml");
            Toml toml = new Toml().read(inputStream);
            staticFile = toml.getString("files.static_input", NO_VALUE_FOUND);
            outputFile = toml.getString("files.output", OUTPUT_FILE);
            eta = toml.getDouble("simulation.eta");
            if (staticFile.equals(NO_VALUE_FOUND))
                throw new Exception("Invalid static file");
            Input input = FileParser.parseFiles(staticFile);

            // Initialize simulation
            OffLatticeSimulation offLatticeSimulation = new OffLatticeSimulation(input, eta);

            // Delete old outputs
            File file = new File(outputFile);
            file.delete();

            // Run simulation
            for (int i = 0; i < 10; i++) {
                offLatticeSimulation.nextState();
                updateOutputFile(outputFile, offLatticeSimulation.getParticles(), offLatticeSimulation.getTime());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void updateOutputFile(String fileName, List<Particle> particles, int time) throws IOException, IOException {
        File file = new File(fileName);
        FileWriter fileWriter = new FileWriter(file, true);

        StringBuilder stringBuilder = new StringBuilder();

        stringBuilder.append(time).append("\n");

        particles.forEach(particle -> stringBuilder.append(String.format("%d %f %f %f %f\n", particle.getId(), particle.getX(), particle.getY(), particle.getV(), particle.getTheta())));

        stringBuilder.append("\n");

        fileWriter.write(stringBuilder.toString());
        fileWriter.close();
    }
}
