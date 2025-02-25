#include <iostream>
using namespace std;
int main() {
int n;
//input the size
cout << "Enter the number of elements in the array: ";
cin >> n;
int arr[n];
//input the elements
cout << "Enter the elements of the array: ";
for (int i = 0; i < n; i++) {
cin >> arr[i];
}
//Bubble Sort logic
for (int i = 0; i < n - 1; i++) {
for (int j = 0; j < n - i - 1; j++) {
if (arr[j] > arr[j + 1]) {
int temp = arr[j];
arr[j] = arr[j + 1];
arr[j + 1] = temp;
}
}
}
//sorted array
cout << "Sorted array in ascending order: ";
for (int i = 0; i < n; i++) {cout << arr[i] << " ";
}
return 0;
}