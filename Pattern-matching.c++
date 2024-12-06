#include <iostream>
#include <string>
using namespace std;

// Function to compute the Longest Prefix Suffix (LPS) array
void computeLPS(const string &pattern, int lps[])
{
  int m = pattern.length();
  int length = 0; // length of the previous longest prefix suffix
  lps[0] = 0;     // LPS of the first character is always 0
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

// Function to search for the pattern in the given text using the KMP algorithm
void KMPsearch(const string &text, const string &pattern)
{
  int n = text.length();
  int m = pattern.length();

  int lps[m]; // LPS array
  computeLPS(pattern, lps);

  int i = 0; // index for text
  int j = 0; // index for pattern

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

// Main function
int main()
{
  string text, pattern;

  cout << "Enter the text: ";
  getline(cin, text);

  cout << "Enter the pattern: ";
  getline(cin, pattern);

  cout << "Searching for pattern '" << pattern << "' in text '" << text << "':\n";
  KMPsearch(text, pattern);

  return 0;
}

/*
// C++ program for Naive Pattern
// Searching algorithm
#include <bits/stdc++.h>
using namespace std;

void search(char* pat, char* txt)
{
  int M = strlen(pat);
  int N = strlen(txt);

  // A loop to slide pat[] one by one
  for (int i = 0; i <= N - M; i++) {
    int j;

    // For current index i, check for pattern match
    for (j = 0; j < M; j++)
      if (txt[i + j] != pat[j])
        break;

    if (j
      == M) // if pat[0...M-1] = txt[i, i+1, ...i+M-1]
      cout << "Pattern found at index " << i << endl;
  }
}

// Driver's Code
int main()
{
  char txt[] = "AABAACAADAABAAABAA";
  char pat[] = "AABA";

  // Function call
  search(pat, txt);
  return 0;
}

*/