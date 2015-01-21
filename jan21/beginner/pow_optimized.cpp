/*
 * optimizing pow for tail recursion, time complexity,
 * and possible overflows
 */
#include <iostream>

using namespace std;

/*
 * pow is now O(log2(n))
 */

long pow_work(long base, long power, long current)
{
  if (power <= 0) {
    return current;
  }
  
  if (power % 2 == 0) {
    return pow_work(base * base, power/2, current);
  } else {
    return pow_work(base, power - 1, current * base);

  }
}

// wrapper for our worker function
long pow(long base, long power)
{
  return pow_work(base, power, 1);
}

int main()
{
  long base, power;
  cout << "Please enter in the base number: ";
  cin >> base;
  cout << "Please enter in the power: ";
  cin >> power;

  cout << "The result of " << base << '^' << power << " is " << pow(base, power) << endl;
  return 0;
}

