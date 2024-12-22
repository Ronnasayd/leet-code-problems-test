from typing import List, Optional


class Solution:
    def reverseVowels(self, s: str) -> str:
        r = []
        ss = []
        for i in range(len(s)):
            ss.append(s[i])
            if s[i].lower() in ["a", "e", "i", "o", "u"]:
                r.append(i)
        r2 = reversed(r)
        for i, j in zip(r[0 : len(r) // 2], r2):
            aux = ss[i]
            ss[i] = ss[j]
            ss[j] = aux
        return "".join(ss)
