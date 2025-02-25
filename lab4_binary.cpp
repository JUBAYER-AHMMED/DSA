#include <iostream>
using namespace std;
int main()
{
  int n, target, left, right, mid, step = 1;
  // taking array size
  cout << "Enter the number of elements: ";
  cin >> n;
  int arr[n];
  // taking sorted array
  cout << "Enter " << n << " sorted elements: ";
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }
  // searching number
  cout << "Enter the number to search: ";
  cin >> target;
  // Binary Search Logic
  left = 0;
  right = n - 1;
  while (left <= right)
  {
    mid = left + (right - left) / 2; // printing the possition
    if (arr[mid] == target)
    {
      cout << "Target " << target << " found at position " << mid + 1 << endl;
      return 0;
    }
    else if (arr[mid] < target)
    {
      left = mid + 1;
    }
    else
    {
      right = mid - 1;
    }
    step++;
  }
  cout << "Target " << target << " not found in the array" << endl;
  return 0;
}