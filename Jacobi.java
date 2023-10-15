public class Jacobi {
    public static void main(String[] args) {
        double a[][] = {{1.0, 0.0, 0.0, 1.0}, {1.0, 1.0, 0.0, 0.0}, {0.0, 1.0, 1.0, -1.0}}; // matriz dos coeficientes
        double b[] = {35.0, 40.0, 30.0}; // matriz dos termos independentes

        double x[] = {0, 0, 0}; // iteração inicial
        int n = 100; // número máximo de iterações
        double tolerancia = 1e-6; // tolerância para o critério de parada

        jacobi(a, b, x, n, tolerancia);
    }

    public static void jacobi(double a[][], double b[], double x[], int n, double tolerance) {
        double next[] = new double[b.length]; // array que armazena a próxima iteração

        for (int k = 0; k < n; k++) {
            boolean converged = true;

            for (int i = 0; i < b.length; i++) {
                double bi = b[i]; // armazena o termo independente da linha i

                for (int j = 0; j < b.length; j++) {
                    if (j != i) {
                        bi -= a[i][j] * x[j]; // multiplicar o valor das variáveis que não foram isoladas
                    }
                }

                bi /= a[i][i];
                System.out.printf("x_%d^(%d) = %.16f\t", i + 1, k + 1, bi);
                next[i] = bi;

                // Verificar convergência
                if (Math.abs(next[i] - x[i]) >= tolerance) {
                    converged = false;
                }
            }

            System.out.println("\n");

            if (converged) {
                System.out.println("O método convergiu após " + (k + 1) + " iterações.");
                break;
            }

            for (int i = 0; i < b.length; i++) {
                x[i] = next[i];
            }
        }
    }
}