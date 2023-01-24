class Node:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        cur = self.head
        for c in word:
            if c not in cur.child.keys():
                cur.child[c] = Node(key = c)    
            cur = cur.child[c]
        cur.data = word

    def search(self, word: str) -> bool:
        cur = self.head
        for c in word:
            if c not in cur.child.keys():
                return False
            cur = cur.child[c]
        
        if cur.data == word:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for c in prefix:
            if c not in cur.child.keys():
                return False
            cur = cur.child[c]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)