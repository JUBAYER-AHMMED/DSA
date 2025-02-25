#include <iostream>
using namespace std;
int main()
{
  int n, key, found = 0;
  // Input the size of the array
  cout << "Enter the number of elements in the array: ";
  cin >> n;
  int arr[n];
  // Input the elements of the array
  cout << "Enter the elements of the array: ";
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }
  // Input the element to search
  cout << "Enter the element to search: ";
  cin >> key;
  // Linear Search Logic
  for (int i = 0; i < n; i++)
  {
    if (arr[i] == key)
    {
      cout << "Element " << key << " found at index " << i << "." << endl;
      found = 1;
      break;
    }
  }
  // If the element is not found
  if (!found)
  {
    cout << "Element " << key << " not found in the array." << endl;
  }
  return 0;
}