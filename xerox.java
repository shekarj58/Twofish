import java.util.*;
class XeroxShop {
public static void main(String[] args) 
{ 	
  Scanner sc = new Scanner(System.in);
 
  System.out.println("Enter the number of copies to be printed:");
  int noOfCopies = sc.nextInt();
  double totalCost;
  double pricePerCopies;

if(noOfCopies > 0 && noOfCopies < 50) {
  pricePerCopies = 2;
  System.out.println("Price per copy: "+"Rs- " +pricePerCopies);
  totalCost = noOfCopies * pricePerCopies; 
}
else if(noOfCopies >= 50 && noOfCopies < 100) {
   pricePerCopies = 1;
   System.out.println("Price per copy: "+"Rs- " +pricePerCopies);
   totalCost = noOfCopies * pricePerCopies;
 }
else if(noOfCopies >= 100 && noOfCopies < 200) {
   pricePerCopies = 0.75;
   System.out.println("Price per copy: " +"Rs- "+pricePerCopies);
   totalCost = noOfCopies * pricePerCopies; 
}
else if(noOfCopies >= 200 && noOfCopies < 500) {
   pricePerCopies = 0.5;
   System.out.println("Price per copy: "+"Rs- " +pricePerCopies);
   totalCost = noOfCopies * pricePerCopies;
   System.out.println("Total cost is "+"$" +totalCost);
}
else {
   pricePerCopies = 0.25;
   System.out.println("Price per copy: "+"Rs- " +pricePerCopies);
   totalCost = noOfCopies * pricePerCopies; 	
  }
  System.out.println("Total cost is "+"Rs- " +totalCost);
 }
}