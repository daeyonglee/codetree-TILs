import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        String c = sc.next();
        double b = sc.nextDouble();
        double a = sc.nextDouble();

        System.out.println(c);
        System.out.println(Utils.round(b));
        System.out.println(Utils.round(a));

    }
}

class Utils {
    public static Boolean checkValue(double d) {
        if (d >= 1 && d <= 1000) {
            return true;
        }
        return false;
    }

    public static Double round(double d) {
        return Math.round(d * 100) / 100.0;
    }
}