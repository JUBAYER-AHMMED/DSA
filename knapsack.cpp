#include <bits/stdc++.h>
using namespace std;

int Knapsack(vector<int> p, vector<int> w, int c, int n)
{
  vector<vector<int>> dp(n + 1, vector<int>(c + 1, 0));

  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= c; j++)
    {
      if (w[i - 1] <= j)
      {
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + p[i - 1]);
      }
      else
      {
        dp[i][j] = dp[i - 1][j];
      }
    }
  }
  return dp[n][c];
}

int main()
{
  int n, capacity;
  cout << "Enter the number of items:";
  cin >> n;

  vector<int> profits(n), weights(n);
  cout << "Enter the profits:";
  for (int i = 0; i < n; i++)
  {
    cin >> profits[i];
  }
  cout << "Enter the weights:";
  for (int i = 0; i < n; i++)
  {
    cin >> weights[i];
  }

  cout << "Enter the capacity:";
  cin >> capacity;
  cout << "Maximum Profit:" << Knapsack(profits, weights, capacity, n);
  return 0;
}
