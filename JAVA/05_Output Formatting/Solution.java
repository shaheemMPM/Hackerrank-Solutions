import java.util.Scanner;

public class Solution {

  public static String repeat(String s, int times) {
    if (times <= 0) return "";
    else return s + repeat(s, times-1);
  }

  public static String format(int n) {
    String res = String.valueOf(n);
    if (res.length() == 1) {
      return "00"+res;
    }else if(res.length() == 2) {
      return "0"+res;
    }
    return res;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("================================");
    for(int i=0;i<3;i++) {
      String s1=sc.next();
      int x=sc.nextInt();
      System.out.println(s1+repeat(" ", (15-s1.length()))+format(x));
    }
    System.out.println("================================");
    sc.close();
  }
}
