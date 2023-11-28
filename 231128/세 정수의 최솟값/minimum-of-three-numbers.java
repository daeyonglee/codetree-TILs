import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        try {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            
            if (a <= b) {
                if (a <= c) {
                    System.out.println(a);
                } else {
                    System.out.println(c);
                }
            } else {
                if (b <= c) {
                    System.out.println(b);
                } else {
                    System.out.println(c);
                }
            }


        } catch (Exception e) {

        }
        
    }
}