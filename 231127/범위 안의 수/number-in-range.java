import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            int a = Integer.parseInt(br.readLine());

            if (a >= 10 && a <= 20) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        } catch (Exception e) {

        }
        
    }
}