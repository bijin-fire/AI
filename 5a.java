import java.util.*;

public class Main {
    public static void main(String[] args) {
        double[][] x = { { 1, -2, 1.5, 0 },
                { 1, -0.5, -2, -1.5 },
                { 0, 1, -1, -1.5 } };
        double[] d = { 1, -1, 1 };
        double c = 1;
        double error = 99999;
        double diff = 0;
        int epoch = 0;
        double[] weight = { 1, -1, 0, 0.5 };
        double[] output = new double[d.length];
        while (error > 0.001 && !Arrays.equals(d, output)) {
            System.out.println("---------------------");
            for (int i = 0; i < output.length; i++) {
                output[i] = 0;
            }
            for (int i = 0; i < x.length; i++) {
                double sum = 0;
                for (int j = 0; j < x[0].length; j++) {
                    sum += x[i][j] * weight[j];
                }
                if (sum > 0)
                    sum = 1;
                else
                    sum = -1;
                output[i] = sum;
                System.out.println("List weight: ");
                for (int k = 0; k < weight.length; k++) {
                    diff = d[i] - output[i];
                    double z = x[i][k];
                    weight[k] += c * diff * z;
                    System.out.print(weight[k] + " ");
                }
                System.out.println("");
            }
            epoch++;
            System.out.println("Epoch:" + epoch);
            error = (double) diff * (double) c;
            System.out.println("actual output: ");
            for (int i = 0; i < output.length; i++) {
                System.out.print(output[i] + " ");
            }
            System.out.println();
        }
    }
}
