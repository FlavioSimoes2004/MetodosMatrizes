public class Jacobi {
    public static void main(String[] args) {
        double a[][] = {{4,1,-1},{-1,3,1},{1,-1,5}}; //matriz dos coeficientes
        double b [] = {5,6,4}; //matriz dos termos independentes

        double x[] = {0,0,0}; // iteração inicial
        int n = 5; //número máximo de iterações

        jacobi(a,b,x,n);


    }
    
    public static void jacobi(double a[][], double b[], double x[], int n) {
        double next[] = {0,0,0}; // array que armazena a proxima iteração
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < b.length;i++) {
                double bi = b[i]; // armazena o termo independente da linha i
                    for (int j = 0; j < b.length; j++) {
                        if (j != i) {
                            bi -= a[i][j] * x[j]; // multiplicar o valor das variaveis que não foram isoladas

                        }
                    }
                    bi /= a[i][i];
                    System.out.printf("x_%d^(%d) = %.16f\t", i + 1, k + 1, bi);
                    next[i] = bi;
            }
            System.out.println("\n");
            for (int i = 0; i < b.length; i++) {
                x[i] = next[i];
            }
        }
    }
}