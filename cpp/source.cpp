#include "my-std-utils.cpp"
#include <algorithm>
#include <bitset>
#include <cmath>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> applyOperations(vector<int> &nums) {
    int n = nums.size();

    // Double adjacent equal elements and set the next to zero
    for (int i = 0; i < n - 1; i++) {
      if (nums[i] == nums[i + 1]) {
        nums[i] *= 2;
        nums[i + 1] = 0;
      }
    }

    // Move non-zero elements to the left
    int left = 0;
    for (int right = 0; right < n; right++) {
      if (nums[right] != 0) {
        swap(nums[left], nums[right]);
        left++;
      }
    }

    return nums;
  }
};
