from typing import List, Optional


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for letter in magazine:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        for letter in ransomNote:
            if letter not in hashmap:
                return False
            elif hashmap[letter] == 0:
                return False
            else:
                hashmap[letter] -= 1
        return True
