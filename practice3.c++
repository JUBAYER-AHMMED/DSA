#include <bits/stdc++.h>
using namespace std;
void merge(int a[], int beg, int mid, int end)
{
  int n1 = mid - beg + 1;
  int n2 = end - mid;
  int leftArray[n1], rightArray[n2];

  // copy
  for (int i = 0; i < n1; i++)
  {
    leftArray[i] = a[beg + i];
  }
  for (int i = 0; i < n1; i++)
  {
    rightArray[i] = a[mid + 1 + i];
  }

  int i = 0;
  int j = 0;
  int k = beg;
  while (i < n1 && j < n2)
  {
    if (leftArray[i] <= rightArray[j])
    {
      a[k] = leftArray[i];
      i++;
    }
    else
    {
      a[k] = rightArray[j];
      j++;
    }
    k++;
  }

  while (i < n1)
  {
    a[k] = leftArray[i];
    i++;
    k++;
  }
  while (j < n2)
  {
    a[k] = rightArray[j];
    j++;
    k++;
  }
}

void merge_sort(int a[], int beg, int end)
{
  if (beg < end)
  {
    int mid = beg + (end - beg) / 2;

    merge_sort(a, beg, mid);
    merge_sort(a, mid + 1, end);

    merge(a, beg, mid, end);
  }
}
int main()
{
  int n;
  cout << "Enter the number of elements : ";
  cin >> n;
  int arr[n];
  cout << "Enter the elements : ";
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }

  merge_sort(arr, 0, n - 1);

  cout << "Sorted array : ";
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
  return 0;
}
