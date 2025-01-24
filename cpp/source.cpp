#include <vector>
#include <string>
#include <map>
#include <tuple>
#include <deque>
#include <stack>
#include "my-std-utils.cpp"

using namespace std;

class Solution
{
public:
  vector<int> eventualSafeNodes(vector<vector<int>> &graph)
  {
    int n = graph.size();
    vector<int> ans;

    for (size_t i = 0; i < n; i++)
    {
      deque<int> q;
      vector<bool> visited(n, false);
      bool getEnd = false;
      q.push_back(i);
      int current;
      int counter = 0;
      while (!q.empty())
      {
        current = q.back();
        q.pop_back();
        visited[current] = true;
        counter++;
        if (graph[current].size() == 0)
        {
          getEnd = true;
        }
        for (auto index : graph[current])
        {
          if (visited[index])
            continue;
          q.push_back(index);
        }
      }
      if (getEnd && counter <= 2)
      {
        ans.push_back(i);
      }
      sort(ans.begin(), ans.end());
    }

    return ans;
  }
};
