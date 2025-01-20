#ifndef MY_STD_UTILS
#define MY_STD_UTILS

#include <iostream>
#include <vector>
#include <string>
#include <sstream>   // For std::istringstream
#include <algorithm> // For std::remove_if

using namespace std;

template <typename T>
void stdoutVector(const vector<T> &v, bool endline = true)
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
bool replace(std::string &str, const std::string &from, const std::string &to)
{
  size_t start_pos = str.find(from);
  if (start_pos == std::string::npos)
    return false;
  str.replace(start_pos, from.length(), to);
  return true;
}

std::vector<std::string> split(std::string &s, std::string &delimiter)
{
  std::vector<std::string> tokens;
  size_t pos = 0;
  std::string token;
  while ((pos = s.find(delimiter)) != std::string::npos)
  {
    token = s.substr(0, pos);
    tokens.push_back(token);
    s.erase(0, pos + delimiter.length());
  }
  tokens.push_back(s);

  return tokens;
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
void stdoutInt(int value, bool endline = true)
{
  cout << value;
  if (endline)
  {
    cout << "\n";
  }
}

template <typename T>
vector<vector<T>> stdinMatrix(string line)
{
  vector<vector<T>> v;
  replace(line, "[[", "");
  replace(line, "]]", "");
  string delimiter = "],[";
  auto tokens = split(line, delimiter);
  for (auto token : tokens)
  {
    auto u = stdinVector<T>(token);
    v.push_back(u);
  }

  return v;
}

void stdoutMatrix(vector<vector<int>> &mat, bool endline = true)
{
  cout << "[";

  for (size_t i = 0; i < mat.size(); ++i)
  {

    stdoutVector(mat[i], false);
    if (i < mat.size() - 1) // Check if it's not the last element
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
#endif
