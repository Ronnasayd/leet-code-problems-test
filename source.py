from typing import List, Optional


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        if flowerbed == [0]:
            return True
        if flowerbed == [0, 0] and n == 1:
            return True
        if flowerbed == [0, 0, 0] and n <= 2:
            return True
        for i in range(0, l + 1 - 3, 1):
            v = flowerbed[i : i + 3]
            if v == [0, 0, 0]:
                if i == 0:
                    flowerbed[i] = 1
                else:
                    flowerbed[i + 1] = 1
                n -= 1
            if v == [0, 0, 1] and flowerbed[max(i - 1, 0)] != 1:
                flowerbed[i] = 1
                n -= 1
            if v == [1, 0, 0] and i + 3 <= l and flowerbed[min(i + 3, l - 1)] != 1:
                flowerbed[i + 2] = 1
                n -= 1
        return max(n, 0) == 0
