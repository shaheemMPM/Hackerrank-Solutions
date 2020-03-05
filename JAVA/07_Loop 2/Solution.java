import java.util.Scanner;
import java.lang.Math;

public class Solution {

  public static String series(int a, int b, int n) {
    int term = a;
    String res = "";
    for(int i = 0; i < n; i++) {
      int temp = term+((int)Math.pow(2, i))*b;
      term = temp;
      res += (String.valueOf(temp)+" ");
    }
    return res;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int q = sc.nextInt();
    for(int i = 0; i < q; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      int n = sc.nextInt();
      System.out.println(series(a, b, n));
    }
    sc.close();
  }
}
