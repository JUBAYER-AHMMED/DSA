#include <iostream>
using namespace std;
void mergeSort(int arr[], int left, int right)
{
  if (left >= right)
    return;
  int mid = left + (right - left) / 2;
  mergeSort(arr, left, mid);
  mergeSort(arr, mid + 1, right);
  int n1 = mid - left + 1, n2 = right - mid;
  int leftArr[n1], rightArr[n2];
  for (int i = 0; i < n1; i++)
    leftArr[i] = arr[left + i];
  for (int j = 0; j < n2; j++)
    rightArr[j] = arr[mid + 1 + j];
  int i = 0, j = 0, k = left;
  while (i < n1 && j < n2)
  {
    arr[k++] = (leftArr[i] <= rightArr[j]) ? leftArr[i++] : rightArr[j++];
  }
  while (i < n1)
    arr[k++] = leftArr[i++];
  while (j < n2)
    arr[k++] = rightArr[j++];
}
int main()
{
  int n;
  cout << "Enter the elemnets number of array : ";
  cin >> n;
  int arr[n];
  cout << "Enter the elements of array : ";
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }
  mergeSort(arr, 0, n - 1);
  cout << "The sorted array is : ";
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
  return 0;
}