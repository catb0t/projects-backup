import java.util.Scanner;

public class droot {

  public static void main (String[] args) {

    Scanner sc = new Scanner(System.in);
    System.out.print("Give me a number! ");
    final Integer g = sc.nextInt();
    System.out.println("Digital root: " + ((~(-g)) % 9 + 1) );

  }

}