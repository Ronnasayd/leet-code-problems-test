#include <iostream>
#include <vector>
#include <string>
#include <sstream>   // For std::istringstream
#include <algorithm> // For std::remove_if

using namespace std;
#include "source.cpp"

template <typename T>
void stdoutVector(const vector<T> &v)
{
  cout << "[";
  for (size_t i = 0; i < v.size(); ++i)
  {
    cout << v[i];
    if (i < v.size() - 1) // Check if it's not the last element
    {
      cout << ",";
    }
  }
  cout << "]\n";
}

template <typename U>
vector<U> stdinVector()
{
  vector<U> v;
  string line;

  // Read a whole line from standard input
  if (getline(cin, line))
  {
    // Remove leading and trailing spaces
    line.erase(remove_if(line.begin(), line.end(), ::isspace), line.end());

    // Check if the input starts with '[' and ends with ']'
    if (line.front() == '[' && line.back() == ']')
    {
      // Remove the brackets
      line = line.substr(1, line.size() - 2);
    }

    istringstream iss(line); // Create a string stream from the modified line
    U input;

    // Read each element from the string stream, separated by commas
    while (getline(iss, line, ','))
    {
      istringstream elementStream(line); // Create a stream for each element
      if (elementStream >> input)
      {
        v.push_back(input);
      }
    }
  }

  return v;
}

int main()
{
  freopen("inputs.txt", "r", stdin);
  freopen("outputs.txt", "w", stdout);
  auto solution = new Solution();
  int a;
  while (!cin.eof())
  {
    auto v = stdinVector<int>();
    cin >> a;
    // Check if the vector is empty; if it is, break the loop
    if (v.empty())
    {
      break;
    }
    stdoutVector(v);
    cout << a << "\n";
  }

  return 0;
}
