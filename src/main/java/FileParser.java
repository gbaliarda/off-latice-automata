import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class FileParser {
    private static Input input;

    public static Input parseFiles(String staticFile) throws FileNotFoundException {
        input = new Input();
        parseStaticFile(staticFile);
        return input;
    }

    private static void parseStaticFile(String staticFile) {
        input.setParticles(new ArrayList<>());
        try (Stream<String> stream = Files.lines(Paths.get(staticFile))) {
            int N = Integer.parseInt(stream.findFirst().get());
            Stream<String> lineStream = Files.lines(Paths.get(staticFile)).skip(1);
            int L = Integer.parseInt(lineStream.findFirst().get());
            lineStream = Files.lines(Paths.get(staticFile)).skip(2);
            double r = Double.parseDouble(lineStream.findFirst().get());
            lineStream = Files.lines(Paths.get(staticFile)).skip(3);

            input.setAmountParticles(N);
            input.setLengthMatrix(L);
            input.setInteractionRadius(r);

            AtomicInteger id = new AtomicInteger(0);
            lineStream.forEach(line -> {
                String[] values = line.split(" ");
                double[] doubles = new double[values.length];
                for (int i = 0; i < values.length; i++) {
                    doubles[i] = Double.parseDouble(values[i]);
                }
                double radius = doubles[0];
                double x = doubles[1];
                double y = doubles[2];
                double v = doubles[3];
                double theta = doubles[4];
                Particle p = new Particle(id.getAndAdd(1), x, y, v, theta, radius);
                input.addParticle(p);
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
