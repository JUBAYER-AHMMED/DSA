#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  cin >> n;
  int Data[n];

  for (int i = 0; i < n; i++)
  {
    cin >> Data[i];
  }

  for (int i = 1; i <= n - 1; i++)
  {
    for (int j = 0; j < n - i; j++)
    {
      if (Data[j] > Data[j + 1])
      {
        int temp = Data[j];
        Data[j] = Data[j + 1];
        Data[j + 1] = temp;
      }
    }
  }

  for (int i = 0; i < n; i++)
  {
    cout << Data[i] << " ";
  }

  cout << endl;

  return 0;
}

// #include <bits/stdc++.h>
// using namespace std;

// int main()
// {
//   int n;
//   cin >> n;
//   int Data[n];

//   for (int i = 0; i < n; i++)
//   {
//     cin >> Data[i];
//   }

//   int cmp = 0;
//   int interchange = 0;

//   for (int i = 1; i <= n - 1; i++)
//   {
//     for (int j = 0; j < n - i; j++)
//     {
//       cmp++;
//       if (Data[j] > Data[j + 1])
//       {
//         int temp = Data[j];
//         Data[j] = Data[j + 1];
//         Data[j + 1] = temp;

//         interchange++;
//       }
//     }
//   }

//   for (int i = 0; i < n; i++)
//   {
//     cout << Data[i] << " ";
//   }

//   cout << "\ncmp = " << cmp << "\ninterchange = " << interchange << endl;

//   return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main()
// {
//   int n;
//   cin >> n;
//   int Data[n];

//   for (int i = 0; i < n; i++)
//   {
//     cin >> Data[i];
//   }

//   int cmp = 0;
//   int interchange = 0;

//   for (int i = 1; i <= n - 1; i++)
//   {
//     for (int j = 0; j < n - i; j++)
//     {
//       cmp++;
//       if (Data[j] > Data[j + 1])
//       {
//         swap(Data[j], Data[j + 1]);

//         interchange++;
//       }
//     }
//   }

//   for (int i = 0; i < n; i++)
//   {
//     cout << Data[i] << " ";
//   }

//   cout << "\ncmp = " << cmp << "\ninterchange = " << interchange << endl;

//   return 0;
// }

// Hybrid sorting
//  #include <bits/stdc++.h>
//  using namespace std;
//  int cmpCount = 0;
//  bool cmp(int l, int r)
//  {
//    cmpCount++;
//    return l < r;
//  }
//  int main()
//  {
//    int n;
//    cin >> n;
//    int Data[n];

//   for (int i = 0; i < n; i++)
//   {
//     cin >> Data[i];
//   }

//   sort(Data, Data + n, cmp);

//   for (int i = 0; i < n; i++)
//   {
//     cout << Data[i] << " ";
//   }

//   cout << "\ncmpCount : " << cmpCount << endl;

//   return 0;
// }
