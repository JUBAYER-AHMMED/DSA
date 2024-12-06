// MERGE_SORT(arr, beg, end)

// if beg < end
// set mid = (beg + end)/2
// MERGE_SORT(arr, beg, mid)
// MERGE_SORT(arr, mid + 1, end)
// MERGE (arr, beg, mid, end)
// end of if

// END MERGE_SORT
#include <bits/stdc++.h>
using namespace std;
/* Function to merge the subarrays of a[] */
void merge(int a[], int beg, int mid, int end)
{
    int i, j, k;
    int n1 = mid - beg + 1;
    int n2 = end - mid;

    int LeftArray[n1], RightArray[n2]; // temporary arrays

    /* copy data to temp arrays */
    for (int i = 0; i < n1; i++)
        LeftArray[i] = a[beg + i];
    for (int j = 0; j < n2; j++)
        RightArray[j] = a[mid + 1 + j];

    i = 0,     /* initial index of first sub-array */
        j = 0; /* initial index of second sub-array */
    k = beg;   /* initial index of merged sub-array */

    while (i < n1 && j < n2)
    {
        if (LeftArray[i] <= RightArray[j])
        {
            a[k] = LeftArray[i];
            i++;
        }
        else
        {
            a[k] = RightArray[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        a[k] = LeftArray[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        a[k] = RightArray[j];
        j++;
        k++;
    }
}

/* Function to implement merge sort */
void merge_sort(int a[], int beg, int end)
{
    if (beg < end)
    {
        int mid = beg + (end - beg) / 2; // Avoid potential overflow
        merge_sort(a, beg, mid);
        merge_sort(a, mid + 1, end);
        merge(a, beg, mid, end);
    }
}

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    int arr[n];
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    merge_sort(arr, 0, n - 1);

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
