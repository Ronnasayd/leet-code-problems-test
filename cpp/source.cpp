#include <vector>
using namespace std;
class Solution
{
public:
  bool doesValidArrayExist(vector<int> &derived)
  {

    int x = 0;
    for (auto i : derived)
    {
      x ^= i;
    }
    if (x != 0)
    {
      return false;
    }
    // 1 ^ 1 = 0
    // 0 ^ 0 = 0
    // 1 ^ 0 = 1
    // 0 ^ 1 = 1
    return true;
  }
};
