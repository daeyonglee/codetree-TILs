import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c;

        a += 8;
        b *= 3;
        c = a*b;

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}