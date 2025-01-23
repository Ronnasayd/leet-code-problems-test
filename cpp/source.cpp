#include <vector>
#include <string>
#include <map>
#include <tuple>
#include <deque>
#include "my-std-utils.cpp"

using namespace std;
class Solution
{
public:
  int eraseOverlapIntervals(vector<vector<int>> &intervals)
  {
    int answer = 0;
    int n = intervals.size();
    sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b)
         { return a[1] < b[1]; });
    int ma = intervals[0][1];

    for (size_t i = 1; i < n; i++)
    {
      auto row = intervals[i];
      if (row[0] < ma)
      {
        answer += 1;
      }
      else
      {
        ma = row[1];
      }
    }

    return answer;
  }
};
