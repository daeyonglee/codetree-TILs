import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        String c = sc.next();
        double b = sc.nextDouble();
        double a = sc.nextDouble();

        System.out.println(c);
        System.out.printf("%.2f\n%.2f", b,a);
    }
}