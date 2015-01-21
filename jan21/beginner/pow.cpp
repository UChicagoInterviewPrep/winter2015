#include <iostream>

using namespace std;

// naive recursive solution
// prone to stack overflow
int pow(int base, int power)
{
  if (power <= 0) {
    return 1;
  } else {
    return base * pow(base, power-1);
  }
}

int main()
{
  int base, power;
  cout << "Please enter in the base number: ";
  cin >> base;
  cout << "Please enter in the power: ";
  cin >> power;

  cout << "The result of " << base << '^' << power << " is " << pow(base, power) << endl;
  return 0;
}
