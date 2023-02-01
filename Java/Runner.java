// package Java;
// import java.io.BufferedReader;
// import java.io.FileNotFoundException;
// import java.io.FileReader;
// import java.io.IOException;
// import java.util.ArrayList;

// import Java.Solution;

// public class Runner {
//     public static void main(String[] args) throws IOException {
//         ArrayList<String> solverArgs = new ArrayList<>();
//         try(BufferedReader br = new BufferedReader(new FileReader("TestFile.txt"))) {
//             String line = br.readLine();
        
//             while (line != null) {
//                 solverArgs.add(line);
//             }
//         }
//         Solution.runSolver(solverArgs);
//         System.out.println("Done.");
//     }
// }
