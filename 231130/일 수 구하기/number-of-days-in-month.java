import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int month = sc.nextInt();

        if (month == 2) {
            System.out.println(28);
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            System.out.println(30);
        } else {
            System.out.println(31);
        }
    }
}