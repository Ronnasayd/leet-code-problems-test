from typing import *


class Node:
    def __init__(self, value=None):
        self.children = {}
        self.is_end = False
        self.value = value


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = Node(letter)
            curr = curr.children[letter]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return True


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:

        prefix = ""
        answer = []

        for letter in searchWord:
            prefix += letter
            aux = []
            for product in products:
                trie = Trie()
                trie.insert(product)
                if trie.startsWith(prefix):
                    aux.append(product)
            products = aux
            answer.append(sorted(aux)[0:3])
        return answer
