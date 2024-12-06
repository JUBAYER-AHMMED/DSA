#include <bits/stdc++.h>
using namespace std;

void computeLPS(const string &pattern, int lps[])
{
  int m = pattern.length();
  int length = 0;
  lps[0] = 0;
  int i = 1;
  while (i < m)
  {
    if (pattern[i] == pattern[length])
    {
      length++;
      lps[i] = length;
      i++;
    }

    else
    {
      if (length != 0)
      {
        length = lps[length - 1];
      }
      else
      {
        lps[i] = 0;
        i++;
      }
    }
  }
}

void KMPsearch(const string &text, const string &pattern)
{
  int n = text.length();
  int m = pattern.length();

  int lps[m];
  computeLPS(pattern, lps);

  int i = 0;
  int j = 0;

  while (i < n)
  {
    if (pattern[j] == text[i])
    {
      i++;
      j++;
    }

    if (j == m)
    {
      cout << "Pattern found at index " << i - j << endl;
      j = lps[j - 1];
    }
    else if (i < n && pattern[j] != text[i])
    {
      if (j != 0)
      {
        j = lps[j - 1];
      }
      else
      {
        i++;
      }
    }
  }
}
int main()
{
  string text, pattern;
  cout << "Enter the text: ";
  getline(cin, text);
  cout << "Enter the pattern: ";
  getline(cin, pattern);

  cout << "Searching for pattern :" << pattern << " in text :" << text << "\n";

  KMPsearch(text, pattern);

  return 0;
}
