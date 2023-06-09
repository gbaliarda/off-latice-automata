import com.moandjiezana.toml.Toml;

import java.io.*;
import java.util.List;
import java.util.Locale;

public class App {
    private static final String NO_VALUE_FOUND = "NO_VALUE_FOUND";
    private static final String OUTPUT_FILE = "output.txt";

    public static void main( String[] args ) {
        String staticFile, outputFile;
        long iterations, N;
        double eta, L;
        try {
            // Configuration
            InputStream inputStream = new FileInputStream("config.toml");
            Toml toml = new Toml().read(inputStream);
            staticFile = toml.getString("files.static_input", NO_VALUE_FOUND);
            outputFile = toml.getString("files.output", OUTPUT_FILE);
            N = toml.getLong("simulation.N");
	    L = toml.getDouble("simulation.L");
	    eta = toml.getDouble("simulation.eta");
            iterations = toml.getLong("simulation.iterations");
            if (staticFile.equals(NO_VALUE_FOUND))
                throw new Exception("Invalid static file");
            Input input = FileParser.parseFiles(staticFile);
	    input.setAmountParticles(N);
	    input.setL(L);
            // Initialize simulation
            OffLatticeSimulation offLatticeSimulation = new OffLatticeSimulation(input, eta);

            // Delete old outputs
            File file = new File(outputFile);
            file.delete();

            // Run simulation
            for (int i = 0; i < iterations; i++) {
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

        particles.forEach(particle -> stringBuilder.append(String.format(Locale.US ,"%d %f %f %f %f\n", particle.getId(), particle.getX(), particle.getY(), particle.getV(), particle.getTheta())));

        fileWriter.write(stringBuilder.toString());
        fileWriter.close();
    }
}
