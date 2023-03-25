import com.moandjiezana.toml.Toml;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.List;
import java.util.Map;

public class App {
    private static final String NO_VALUE_FOUND = "NO_VALUE_FOUND";

    public static void main( String[] args ) {
        String staticFile;
        try {
            InputStream inputStream = new FileInputStream("config.toml");
            Toml toml = new Toml().read(inputStream);
            staticFile = toml.getString("files.static_input", NO_VALUE_FOUND);

            if (staticFile.equals(NO_VALUE_FOUND))
                throw new Exception("Invalid static or dynamic file");
        } catch (Exception e) {
            System.out.println("Error while reading configuration file");
            return;
        }

        try {
            Input input = FileParser.parseFiles(staticFile);
            CellIndexMethod t = new CellIndexMethod(input.getParticles(), input.getLengthMatrix(), true);
            Map<Particle, List<Particle>> output = t.computeNeighbourhoods();
            output.forEach((p, list) -> {
                System.out.println(p.getId() + " " + list.size());
            });
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}
