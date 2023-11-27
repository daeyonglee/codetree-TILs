import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            float a = Float.parseFloat(br.readLine());
            float b = Float.parseFloat(br.readLine());

            if (a >= 1.0f && b >= 1.0f) {
                System.out.println("High");
            } else if (a >= 0.5f && b >= 0.5f) {
                System.out.println("Middle");
            } else {
                System.out.println("Low");
            }
        } catch (Exception e) {

        }
    }
}