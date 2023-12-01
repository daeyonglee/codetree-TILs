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
    int[] tempArr = arr;

    for (int i = 0; i < arr.length; i++) {
      for (int j = 0; j <= i-1; j++) {
        if(tempArr[j] < arr[i]) {
          int a = tempArr[j];
          tempArr[j] = arr[i];
          tempArr[i] = a;
        }
      }
    }


    return tempArr;
  }
}