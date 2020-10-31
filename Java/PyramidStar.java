import java.util.Scanner;

public class PyramidStar{

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter height of pyramid");
        int n = scanner.nextInt();
        int i=1;
        while(i<=n){
            int j=1;
            while(j<=n-i){
                System.out.print(" ");
                j+=1;
            }
            j=1;
            while(j<=i){
                System.out.print("*");
                j+=1;
            }
            j=1;
            while (j<i){
                System.out.print("*");
                j+=1;
            }
            i+=1;
            System.out.println();
        }
    }
}