import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int aAge = sc.nextInt();
        String aGender = sc.next();
        int bAge = sc.nextInt();
        String bGender = sc.next();

        if ((aAge >= 19 && aGender.equals("M")) || (bAge >= 19 && bGender.equals("M"))) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }


    }
}