class Solution
{
public:
  int minimizeXor(int num1, int num2)
  {
    int cnum1 = __popcount(num1);
    int cnum2 = __popcount(num2);
    while (cnum1 > cnum2)
    {
      num1 &= (num1 - 1);
      cnum1 = __popcount(num1);
    }
    while (cnum1 < cnum2)
    {
      num1 |= (num1 + 1);
      cnum1 = __popcount(num1);
    }
    return num1;
  }
};
