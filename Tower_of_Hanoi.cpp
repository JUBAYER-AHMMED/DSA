#include <bits/stdc++.h>
using namespace std;
int moves = 0;
void TowerOfHanoi(int n, char src, char helper, char dst)
{
  if (n == 1)
  {
    cout << "Move a disk from " << src << " to " << dst << endl;
    moves++;
    return;
  }

  TowerOfHanoi(n - 1, src, dst, helper);
  cout << "Move a disk from " << src << " to " << dst << endl;
  TowerOfHanoi(n - 1, helper, src, dst);
  moves++;
}

int main()
{
  int n;

  cout << "Enter the number of disk: ";
  cin >> n;
  TowerOfHanoi(n, 'S', 'H', 'D');
  cout << "Total moves: " << moves << endl;
  return 0;
}
