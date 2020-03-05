import java.util.Scanner;

public class Solution {

  public static String format(int n, int i) {
    return String.valueOf(n)+" x "+String.valueOf(i)+" = "+String.valueOf(n*i);
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for(int i = 1; i <= 10; i++){
      System.out.println(format(n, i));
    }
    sc.close();
  }
}
