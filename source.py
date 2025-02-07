from typing import *


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return s.trim().split(" ")[-1]
