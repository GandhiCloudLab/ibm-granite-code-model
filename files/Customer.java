public class Customer {

    public String firstName;

    public String lastName;
    
    public Customer (String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    
    //Write a method to find a factorial of a given number
    public int findFactorial(int n) {
        if (n == 0)
            return 1;
        else
            return n * findFactorial(n - 1);
    }
}