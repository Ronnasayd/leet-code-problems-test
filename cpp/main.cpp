
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
    auto intervals = stdinMatrix<int>(line);
    auto answer = solution->eraseOverlapIntervals(intervals);
    stdoutRaw(answer);
  }

  return 0;
}
