//código em JAVA
//Método de Gauss Jordan
public class GaussJo{
	
public static double[][] MatGaJo(double[][] Matriz){
	double[][] VMatriz = Matriz;
	double VNum; //variáveis
	
	//operação
	for(int i=0; i<=VMatriz.length-1; i++) {
		VNum = VMatriz [i][i];
		
		for(int j=0; j<=VMatriz[0].length-1; j++) {
			VMatriz[i][j] = VMatriz[i][j]/VNum;
		}
		System.out.println("| "+ VMatriz[0][0] + " " + VMatriz[0][1] + " " + VMatriz[0][2] + " | " + VMatriz[0][3] + " |");
		System.out.println("| "+ VMatriz[1][0] + " " + VMatriz[1][1] + " " + VMatriz[1][2] + " | " + VMatriz[1][3] + " |");
		System.out.println("| "+ VMatriz[2][0] + " " + VMatriz[2][1] + " " + VMatriz[2][2] + " | " + VMatriz[2][3] + " |");
		System.out.println("");
		if(i<=VMatriz.length-2) {
			for(int j=i+1; j<=VMatriz.length-1; j++) {
				VNum = VMatriz[j][i];
				
				for(int k=0; k<=VMatriz[0].length-1; k++) {
					VMatriz[j][k] = (VMatriz[j][k]-(VNum*VMatriz[i][k]));
					
				}
				System.out.println("| "+ VMatriz[0][0] + " " + VMatriz[0][1] + " " + VMatriz[0][2] + " | " + VMatriz[0][3] + " |");
				System.out.println("| "+ VMatriz[1][0] + " " + VMatriz[1][1] + " " + VMatriz[1][2] + " | " + VMatriz[1][3] + " |");
				System.out.println("| "+ VMatriz[2][0] + " " + VMatriz[2][1] + " " + VMatriz[2][2] + " | " + VMatriz[2][3] + " |");
				System.out.println("");
			}
		}
		
	}
	
	for(int i=VMatriz.length-1; i>=1; i--) {
		for(int j=i-1 ; j>=0; j--) {
			VNum = VMatriz[j][i];
			
			for(int k=VMatriz[0].length-1; k>=0; k--) {
				VMatriz[j][k] = (VMatriz[j][k]-(VNum*VMatriz[i][k]));
				
			}
			System.out.println("| "+ VMatriz[0][0] + " " + VMatriz[0][1] + " " + VMatriz[0][2] + " | " + VMatriz[0][3] + " |");
			System.out.println("| "+ VMatriz[1][0] + " " + VMatriz[1][1] + " " + VMatriz[1][2] + " | " + VMatriz[1][3] + " |");
			System.out.println("| "+ VMatriz[2][0] + " " + VMatriz[2][1] + " " + VMatriz[2][2] + " | " + VMatriz[2][3] + " |");
			System.out.println("");
		}
		
	}
	
	return VMatriz;
}

public static void main(String[] args) {
	double A[][] = {
			{3, -2, 5, 2},
			{2, 4, -1, 2},
			{-7, -3, 4, 2}
	};
	System.out.println("| "+ A[0][0] + " " + A[0][1] + " " + A[0][2] + " | " + A[0][3] + " |");
	System.out.println("| "+ A[1][0] + " " + A[1][1] + " " + A[1][2] + " | " + A[1][3] + " |");
	System.out.println("| "+ A[2][0] + " " + A[2][1] + " " + A[2][2] + " | " + A[2][3] + " |");
	System.out.println("");
	
	MatGaJo(A);
	
}
}
