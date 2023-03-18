#include <iostream>

int main() {

      
  int year = 0;

  std::cout << "This program lets you know whether a year is a leap year or not\n";
  std::cout << "What year would you like to test?: ";
  std::cin >> year;

  if (year < 1000 or year > 9999) {
    std::cout << "Invalid entry.\n";
  }

  if (year % 4 == 0 and year % 100 !=0 or year % 400 ==0)  {
   std::cout << year << " falls on a leap year\n"; 
  }
  
  else {
    std::cout << year << " is not a leap year\n";
  }
  

}