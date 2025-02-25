#include <iostream>
#include <cmath>
using namespace std;
int main()
{
  int N, target_sum;
  cout << "Enter the number of elements: ";
  cin >> N;
  int S[N];
  cout << "Enter the elements: ";
  for (int i = 0; i < N; i++)
  {
    cin >> S[i];
  }
  cout << "Enter the target sum: ";
  cin >> target_sum;
  int total_subsets = 1 << N;
  int count = 0;
  for (int mask = 0; mask < total_subsets; mask++)
  {
    int subset_sum = 0;
    bool found = false;
    for (int j = 0; j < N; j++)
    {
      if (mask & (1 << j))
      {
        subset_sum += S[j];
      }
    }
    if (subset_sum == target_sum)
    {
      found = true;
      cout << "{ ";
      for (int j = 0; j < N; j++)
      {
        if (mask & (1 << j))
        {
          cout << S[j] << " ";
        }
      }
      cout << "}\n";
      count++;
    }
  }
  cout << "Total subsets found: " << count << endl;
  return 0;
}
