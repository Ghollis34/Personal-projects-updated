package tutorial;
import java.util.Scanner; //This module has to be imported for user input to work

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//System.out.println("Hello World!"); //semi colons must be added at the end of each line of code
		//System.out.println("Hello World!2");
		
		//Variables and Data types
		//The data types in orange are known as primitive and are not changeable
		//int hello_world = 5;//the int describes that it is a number variable type
		//double num2 = 5.0;//double is anything that has a decimal point
		//boolean b = true;//Boolean is either true or false
		//char c = 'h';//a character that has to be placed in single quotation marks, they can only be one character
		//A string is not primitive
		//String str = "tim"; //For strings there are in "" and are defined by using the String data type 		
		//int tim = hello_world;		
		//System.out.println(tim);
		
		//Basic Operators
		//int x = 5;
		//int y = 7;
		//int z = 57;
		//int x = 56 % 5; //Modulus function gives the remainder of the division of the two numbers
		//double u = z / (double)y;//When dividing if two integers are divided by each other then the output will be an integer, so one of the values have to be a double. //Typecasting can be done also to convert the type of the variable in the format: (type)variable
		//double d = Math.pow(x, y); //exponents have to be in the form double, this raises x to the power of y 		
		//System.out.println(u);
		
		//Input and Scanners
		Scanner sc = new Scanner(System.in); //Scanner is a data-type just like string, sc is the name of the datatype, it's equal to a new scanner which is = to System.in, which is user input/typing on the keyboard
		//String scanned = sc.next(); //A new string variable is made called scanned that is getting the next stream of input from the user
		//int scanned = sc.nextInt();//The nextInt has to be used to grab an integer value from the user
		//boolean scanned = sc.nextBoolean();
		String scanned = sc.next();//It should always be set to a string as a string can be anything
		int x = Integer.parseInt(scanned);//This integer.parseint is needed to convert the string to an integer
		
		System.out.println(x);
	}

}
