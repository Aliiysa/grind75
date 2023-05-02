class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True
    
    def search(self, word):
        cur = self.root

        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord
    
    def startsWith(self, prefix):
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True