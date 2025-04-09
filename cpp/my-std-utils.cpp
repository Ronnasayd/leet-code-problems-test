#ifndef MY_STD_UTILS
#define MY_STD_UTILS

#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <sstream>   // For std::istringstream
#include <algorithm> // For std::remove_if
#include <typeinfo>
#include <map>
#include <type_traits>

using namespace std;

template <typename T>
void stdoutVector(const T &v, bool endline = true, bool isLog = false)
{
  if (isLog)
  {
    cout << "[log]:";
  }

  cout << "[";
  int counter = 0;
  for (auto &&i : v)
  {
    cout << i;
    if (counter < v.size() - 1) // Check if it's not the last element
    {
      cout << ",";
    }
    counter++;
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

void replaceAll(std::string &str, const std::string &from, const std::string &to)
{
  if (from.empty())
    return;
  size_t start_pos = 0;
  while ((start_pos = str.find(from, start_pos)) != std::string::npos)
  {
    str.replace(start_pos, from.length(), to);
    start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
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
        //replaceAll(input, "'", "");
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
template <typename T>
void stdoutRaw(T value, bool endline = true, bool isLog = false)
{
  if (isLog)
  {
    cout << "[log]:";
  }
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
template <typename T>
void stdoutMatrix(vector<vector<T>> &mat, bool endline = true, bool isLog = false)
{
  if (isLog)
  {
    cout << "[log]:";
  }
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
template <typename T>
bool isVector(const T &)
{
  return std::is_same<T, std::vector<typename T::value_type, typename T::allocator_type>>::value;
}

void logAll()
{
  cout << "\n";
}
void printByContext()
{
}
template <typename T, typename... Args>
void printByContext(T x, Args... args)
{
  if constexpr (is_same_v<T, vector<int>> || is_same_v<T, vector<bool>> || is_same_v<T, vector<string>> || is_same_v<T, set<int>> || is_same_v<T, set<bool>> || is_same_v<T, set<string>>)
  {
    stdoutVector(x, false, false);
  }

  else if constexpr (is_same_v<T, vector<vector<int>>> || is_same_v<T, vector<vector<bool>>> || is_same_v<T, vector<vector<string>>>)
  {
    stdoutMatrix(x, false, false);
  }
  else
  {
    stdoutRaw(x, false, false);
  }

  printByContext(args...);
}
template <typename T, typename... Args>
void logAll(T x, Args... args)
{
  if constexpr (is_same_v<T, vector<int>> || is_same_v<T, vector<bool>> || is_same_v<T, vector<string>> || is_same_v<T, set<int>> || is_same_v<T, set<bool>> || is_same_v<T, set<string>>)
  {
    stdoutVector(x, false, true);
  }
  else if constexpr (is_same_v<T, vector<vector<int>>> || is_same_v<T, vector<vector<bool>>> || is_same_v<T, vector<vector<string>>>)
  {
    stdoutMatrix(x, false, true);
  }
  else
  {
    stdoutRaw(x, false, true);
  }

  logAll(args...);
}

template <typename T, typename U>
void stdoutMap(const map<T, U> &mp, bool endline = true, bool isLog = false)
{
  if (isLog)
  {
    cout << "[log]:";
  }
  cout << "{";

  for (auto it = mp.begin(); it != mp.end();)
  {
    cout << it->first << ":";
    printByContext(it->second);
    if (++it != mp.cend()) // Avoid trailing comma
    {
      cout << ",";
    }
  }

  cout << (endline ? "}\n" : "}");
}

#endif
