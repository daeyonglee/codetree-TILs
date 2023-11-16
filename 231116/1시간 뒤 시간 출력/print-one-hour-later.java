import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        sc.useDelimiter(":");

        int a = sc.nextInt();
        int b = sc.nextInt();

        if (a >= 1 && a <= 22 && b >= 0 && b < 60) {
            System.out.println((a + 1) + ":" + b);
        }
        
    }
}