
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
    auto n = stdinInt(line);
    auto answer = solution->numTilings(n);
    cout << answer << "\n";
  }

  return 0;
}
