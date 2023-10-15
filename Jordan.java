//código em JAVA
//Método de Gauss Jordan
public class Jordan{	

	public static double[][] MatGaJo(double[][] Matriz){
	int loop=0;
	double[][] VMatriz = Matriz;
	double VNum; //variáveis
	
	//operação
	for(int i=0; i<=VMatriz.length-1; i++) {
		VNum = VMatriz [i][i];
		
		for(int j=0; j<=VMatriz[0].length-1; j++) {
			VMatriz[i][j] = VMatriz[i][j]/VNum;
		}
		while(loop==0) {
			for(int a=0; a<VMatriz.length; a++) {
				System.out.print("| ");
				for(int b=0; b<VMatriz[0].length; b++) {
					System.out.print(VMatriz[a][b] + ", ");
				}
				System.out.print("|");
				System.out.println(" ");
				
			}
			System.out.println("-------------");
			loop++;
		}
		loop=0;
		if(i<=VMatriz.length-2) {
			for(int j=i+1; j<=VMatriz.length-1; j++) {
				VNum = VMatriz[j][i];
				
				for(int k=0; k<=VMatriz[0].length-1; k++) {
					VMatriz[j][k] = (VMatriz[j][k]-(VNum*VMatriz[i][k]));
					
				}
				while(loop==0) {
					for(int a=0; a<VMatriz.length; a++) {
						System.out.print("| ");
						for(int b=0; b<VMatriz[0].length; b++) {
							System.out.print(VMatriz[a][b] + ", ");
						}
						System.out.print("|");
						System.out.println(" ");
						
					}
					System.out.println("-------------");
					loop++;
				}
				loop=0;
			}
		}
		
	}
	
	for(int i=VMatriz.length-1; i>=1; i--) {
		for(int j=i-1 ; j>=0; j--) {
			VNum = VMatriz[j][i];
			
			for(int k=VMatriz[0].length-1; k>=0; k--) {
				VMatriz[j][k] = (VMatriz[j][k]-(VNum*VMatriz[i][k]));
				
			}
			while(loop==0) {
				for(int a=0; a<VMatriz.length; a++) {
					System.out.print("| ");
					for(int b=0; b<VMatriz[0].length; b++) {
						System.out.print(VMatriz[a][b] + ", ");
					}
					System.out.print("|");
					System.out.println(" ");
					
				}
				System.out.println("-------------");
				loop++;
			}
			loop=0;
		}
		
	}
	
	return VMatriz;
}

public static void main(String[] args) {
	int loop=0;
	double A[][] = {
			{1, 0, 0, 1, 35},
			{1, 1, 0, 0, 40},
			{0, 1, 1, -1, 30}
	};
	while(loop==0) {
		for(int a=0; a<A.length; a++) {
			System.out.print("| ");
			for(int b=0; b<A[0].length; b++) {
				System.out.print(A[a][b] + ", ");
			}
			System.out.print("|");
			System.out.println(" ");
			
		}
		System.out.println("-------------");
		loop++;
	}
	
	MatGaJo(A);
	
}
}