import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[] arr = new int[3];

    for (int i = 0; i < 3; i++) {
      arr[i] = sc.nextInt();
    }

    int[] sortedArr = sort(arr);

    System.out.println(sortedArr[1]);
    
  }

  public static int[] sort(int[] arr) {
    int[] tempArr = {0, 0, 0};

    for (int i = 0; i < arr.length; i++) {
      if (tempArr[0] == 0) {
        tempArr[0] = arr[0];
        continue;
      }

      for (int j = 0; j <= i-1; j++) {
        int a = tempArr[j];
        if(tempArr[j] < arr[i]) {
          tempArr[j] = arr[i];
          tempArr[j+1] = a;
          break;
        } 
      }
    }


    return tempArr;
  }
}