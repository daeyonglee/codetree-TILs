import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        // BMI = kg / cm^2

        int cm = sc.nextInt();
        float m = cm / 100.0f;
        int kg = sc.nextInt();
        int bmi = (int) (kg / (m*m));

        System.out.println( bmi);
        if (bmi >= 25) {
            System.out.println("Obesity");
        }

    }
}