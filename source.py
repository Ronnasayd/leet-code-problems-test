from typing import *


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        f = n * [0]
        answer = []
        for a, b in zip(A, B):
            f[a - 1] += 1
            f[b - 1] += 1
            answer.append(f.count(2))
        return answer
