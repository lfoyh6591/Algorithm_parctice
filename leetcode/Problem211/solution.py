class trie:
    def __init__(self, finish = False):
        self.child = {}
        self.finish = finish

class WordDictionary:
    def __init__(self):
        self.root = trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word[:-1]:
            if cur.child.get(c, None) is None:
                cur.child[c] = trie()
            cur = cur.child[c]

        if cur.child.get(word[-1], None) is None:
            cur.child[word[-1]] = trie(True)
        else:
            cur.child[word[-1]].finish = True

    def rec_search(self, r, w):
        if len(w) == 1:
            if w == ".":
                if not r.child:
                    return False
                else:
                    for v in r.child.values():
                        if v.finish:
                            return True
                    return False
            return r.child.get(w, trie()).finish
        
        if w[0] != '.':
            if r.child.get(w[0], None) is None:
                return False
            else:
                return self.rec_search(r.child[w[0]], w[1:])
        else:
            ret = False
            for v in r.child.values():
                ret = ret | self.rec_search(v, w[1:])
            return ret

        return True

    def search(self, word: str) -> bool:
        return self.rec_search(self.root, word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)