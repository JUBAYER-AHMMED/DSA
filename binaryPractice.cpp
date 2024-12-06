#include <bits/stdc++.h>
using namespace std;

int BinarySearch(int a[], int beg, int end, int val)
{
  while (beg <= end)
  {
    int mid = beg + (end - beg) / 2;
    if (a[mid] == val)
    {
      return mid;
    }

    else if (a[mid] < val)
      beg = mid + 1;

    else if (a[mid] > val)
    {
      end = mid - 1;
    }
  }

  return -1;
}
int main()
{
  int n;
  cout << "How many numbers: ";
  cin >> n;

  int a[n];
  cout << "Enter the elements: ";
  for (int i = 0; i < n; i++)
  {
    cin >> a[i];
  }
  int x;
  cout << "Enter The Finding Val : ";
  cin >> x;
  int result = BinarySearch(a, 0, n - 1, x);

  if (result == -1)
  {
    cout << "Not Found" << endl;
  }

  else
  {
    cout << "Fount at index : " << result + 1 << endl;
  }

  return 0;
}
