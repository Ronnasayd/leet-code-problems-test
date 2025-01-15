#include <iostream>
#include <vector>
#include <string>
#include <sstream>   // For std::istringstream
#include <algorithm> // For std::remove_if

using namespace std;
#include "source.cpp"

template <typename T>
void stdoutVector(const vector<T> &v, bool endline = false)
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
  if (endline)
  {
    cout << "]\n";
  }
  else
  {
    cout << "]";
  }
}

template <typename U>
vector<U> stdinVector(string line)
{
  vector<U> v;

  // Read a whole line from standard input
  if (line != "")
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

int stdinInt(string line)
{
  return stoi(line);
}
int main()
{
  string line;
  auto solution = new Solution();
  freopen("inputs.txt", "r", stdin);
  freopen("outputs.txt", "w", stdout);
  while (!cin.eof())
  {
    getline(cin, line);
    auto piles = stdinVector<int>(line);
    getline(cin, line);
    auto a = stdinInt(line);
    auto answer = solution->minEatingSpeed(piles, a);
    cout << answer << "\n";
  }

  return 0;
}
