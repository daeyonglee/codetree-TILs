import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        Object[] obj = new Object[3];
        int count = 0;


        for (int i = 0; i < obj.length; i++) {
            String a = sc.next();
            int b = sc.nextInt();

            if (a.equals("Y")) {
                if (b >= 37) {
                    count++;
                } 
            }
        }

        if (count >= 2) {
            System.out.println("E");
        } else {
            System.out.println("N");
        }

        
    }
}