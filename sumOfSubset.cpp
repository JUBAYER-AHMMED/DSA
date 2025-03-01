#include <bits/stdc++.h>
using namespace std;

void sumOfSubset(vector<int> &arr, vector<int> &subset, int sum, int target, int index)
{
  if (sum == target)
  {
    for (int i : subset)
    {
      cout << i << " ";
    }
    cout << endl;
    return;
  }

  for (int i = index; i < arr.size(); i++)
  {
    if (sum + arr[i] <= target)
    {
      subset.push_back(arr[i]);
      sumOfSubset(arr, subset, sum + arr[i], target, i + 1);

      subset.pop_back();
    }
  }
}
int main()
{
  int n, target;
  cout << "Enter the number of elements: ";
  cin >> n;
  vector<int> arr(n);
  cout << "Enter the elements: ";
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }

  cout << "Enter the target sum : ";
  cin >> target;

  vector<int> subset;

  sumOfSubset(arr, subset, 0, target, 0);

  return 0;
}
