#include <iostream>
using namespace std;
#define N 4
void printSolution(int placed[])
{
  static int solutionCount = 0;
  cout << "\nSolution " << ++solutionCount << ":\n";
  for (int i = 0; i < N; i++, cout << "\n")
    for (int j = 0; j < N; j++)
      cout << (placed[i] == j ? 'Q' : '.') << " ";
}
bool isSafe(int placed[], int row, int col)
{
  for (int prev = 0; prev < row; prev++)
  {
    if (placed[prev] == col ||
        placed[prev] - prev == col - row ||
        placed[prev] + prev == col + row)
    {
      return false;
    }
  }
  return true;
}
void solveNQueens(int placed[], int row)
{
  if (row == N)
  {
    printSolution(placed);
    return;
  }
  for (int col = 0; col < N; col++)
  {
    if (isSafe(placed, row, col))
    {
      placed[row] = col;
      solveNQueens(placed, row + 1);
    }
  }
}
int main()
{
  int placed[N] = {-1};
  solveNQueens(placed, 0);
  return 0;
}