#include <iostream>
using namespace std;
int main()
{
  int num;
  char source, destination, auxiliary;
  // Prompting user for input
  cout << "Enter the number of disks: ";
  cin >> num;
  cout << "Enter the source peg, destination peg, and auxiliary peg: ";
  cin >> source >> destination >> auxiliary;
  int total_moves = (1 << num) - 1; // Calculate total moves
  cout << "Total number of moves: " << total_moves << endl;
  int stack[1000][4];
  int top = -1;
  stack[++top][0] = num;
  stack[top][1] = source;
  stack[top][2] = destination;
  stack[top][3] = auxiliary;
  while (top >= 0)
  {
    int n = stack[top][0];
    char from_peg = stack[top][1];
    char to_peg = stack[top][2];
    char aux_peg = stack[top--][3];
    if (n == 1)
    {
      cout << from_peg << " -> " << to_peg << endl;
    }
    else
    {
      stack[++top][0] = n - 1;
      stack[top][1] = aux_peg;
      stack[top][2] = to_peg;
      stack[top][3] = from_peg;
      stack[++top][0] = 1;
      stack[top][1] = from_peg;
      stack[top][2] = to_peg;
      stack[top][3] = aux_peg;
      stack[++top][0] = n - 1;
      stack[top][1] = from_peg;
      stack[top][2] = aux_peg;
      stack[top][3] = to_peg;
    }
  }
  return 0;
}