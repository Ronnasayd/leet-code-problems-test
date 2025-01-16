#include <vector>
using namespace std;
const int MOD = 1000000007; // Define the modulus
class Solution
{
public:
  vector<long long> ways;

  int numTilings(int n)
  {

    if (n == 0)
    {
      return 0;
    }
    if (n == 1)
    {
      return 1;
    }
    if (n == 2)
    {
      return 2;
    }
    if (n == 3)
    {
      return 5;
    }
    this->ways = vector<long long>(n + 1, 0);
    this->ways[1] = 1;
    this->ways[2] = 2;
    this->ways[3] = 5;

    for (int i = 4; i <= n; i++)
    {
      this->ways[i] = (this->ways[i - 3] + 2 * this->ways[i - 1]) % MOD;
    }
    return this->ways[n];
  }
};
