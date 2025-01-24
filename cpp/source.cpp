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
  std::vector<int> eventualSafeNodes(std::vector<std::vector<int>> &graph)
  {
    int n = graph.size();
    std::vector<int> ans;
    std::vector<bool> onPath(n, false); // To detect cycles
    std::vector<bool> safe(n, false);   // To mark safe nodes

    auto dfs = [&](int node, auto &&dfs) -> bool
    {
      if (safe[node])
        return true; // Already determined safe
      if (onPath[node])
        return false; // Found a cycle

      onPath[node] = true; // Mark the node as being visited in the current path
      for (int neighbor : graph[node])
      {
        if (!dfs(neighbor, dfs)) // If any neighbor is not safe
        {
          return false; // Current node is not safe
        }
      }
      onPath[node] = false; // Backtrack
      safe[node] = true;    // Mark as safe
      return true;
    };

    for (int i = 0; i < n; i++)
    {
      if (dfs(i, dfs))
      {
        ans.push_back(i); // If the node is safe, add to result
      }
    }

    std::sort(ans.begin(), ans.end()); // Sort the result before returning
    return ans;
  }
};
