
#include "my-std-utils.cpp"
#include "source.cpp"

int main()
{
  string line;
  auto solution = new Solution();
  freopen("inputs.txt", "r", stdin);
  freopen("outputs.txt", "w", stdout);
  while (!cin.eof())
  {
    getline(cin, line);
    auto n = stdinVector<int>(line);
    auto answer = solution->doesValidArrayExist(n);
    if (answer)
    {
      cout << "true" << "\n";
    }
    else
    {
      cout << "false" << "\n";
    }
  }

  return 0;
}
