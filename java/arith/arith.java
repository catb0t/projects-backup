import java.util.Scanner;

interface arith {
  static void main(String[] args) {
    System.out.print("Type some stupid number ");

    int myNumber = (new Scanner(System.in)).nextInt();

    int a = (myNumber / myNumber) + myNumber - 1;

    System.out.println("Your number is " + a);
  }

}


/*

Question 1
Choose a number. Add 3. Multiply by 2. Add 4. Divide by 2. Subtract the number you started with. The result is ??
the result is 5: 5 3 + 2 * 4 + 2 / 5 - 5 = is t.
Question 2
Choose a number. Double it. Add 9. Add the number you started with. Divide by 3. Add 4. Subtract the number you started with. The result is ??
the result is 12, for input 5
Question 3
Create a trick of your own. You must prove, using algebra, that your trick will always work.
*/