
#include "my-std-utils.cpp"
#include "source.cpp"

int main()
{
  string line;
  auto solution = new Solution();
  freopen("inputs.txt", "r", stdin);
  // freopen("outputs.txt", "w", stdout);
  while (!cin.eof())
  {
    getline(cin, line);
    auto arr = stdinVector<int>(line);
    getline(cin, line);
    auto mat = stdinMatrix<int>(line);
    auto answer = solution->firstCompleteIndex(arr, mat);
    stdoutInt(answer);
  }

  return 0;
}
