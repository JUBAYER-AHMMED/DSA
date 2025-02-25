#include <iostream>
using namespace std;
int main()
{
  int profits[100], weights[100];
  int dp[101][101];
  int n, capacity;
  cout << "Enter the number of items: ";
  cin >> n;
  cout << "Enter the profits of the items:\n";
  for (int i = 0; i < n; i++)
  {
    cin >> profits[i];
  }
  cout << "Enter the weights of the items:\n";
  for (int i = 0; i < n; i++)
  {
    cin >> weights[i];
  }
  cout << "Enter the capacity of the knapsack: ";
  cin >> capacity;
  for (int i = 0; i <= n; i++)
  {
    for (int w = 0; w <= capacity; w++)
    {
      if (i == 0 || w == 0)
      {
        dp[i][w] = 0;
      }
      else if (weights[i - 1] <= w)
      {
        dp[i][w] = (profits[i - 1] + dp[i - 1][w - weights[i - 1]] > dp[i - 1][w]) ? profits[i - 1] + dp[i - 1][w - weights[i - 1]] : dp[i - 1][w];
      }
      else
      {
        dp[i][w] = dp[i - 1][w];
      }
    }
  }
  cout << "DP Table:\n";
  for (int i = 0; i <= n; i++)
  {
    for (int w = 0; w <= capacity; w++)
    {
      cout << dp[i][w] << " ";
    }
    cout << endl;
  }
  int w = capacity;
  cout << "\nItems included to achieve maximum profit:\n";
  for (int i = n; i > 0; i--)
  {
    if (dp[i][w] != dp[i - 1][w])
    {
      cout << "Item " << i << " (Profit: " << profits[i - 1] << ", Weight: " << weights[i - 1]
           << ")\n";
      w = w - weights[i - 1];
    }
  }
  cout << "Maximum profit in the knapsack: " << dp[n][capacity] << endl;
  return 0;
}