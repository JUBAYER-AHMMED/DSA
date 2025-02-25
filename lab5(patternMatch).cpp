#include <iostream>
#include <cstring>
using namespace std;
int main()
{
  char text[1000], pattern[1000];
  cout << "Enter the text: ";
  cin.getline(text, sizeof(text));
  cout << "Enter the pattern: ";
  cin.getline(pattern, sizeof(pattern));
  int textLen = strlen(text);
  int patternLen = strlen(pattern);
  for (int i = 0; i <= textLen - patternLen; i++)
  {
    int j = 0;
    while (j < patternLen && text[i + j] == pattern[j])
    {
      j++;
    }
    if (j == patternLen)
    {
      cout << "Pattern found at index " << i << endl;
      return 0;
    }
  }
  cout << "Pattern not found in the text" << endl;
  return 0;
}