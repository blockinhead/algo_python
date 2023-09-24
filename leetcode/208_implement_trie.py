class Trie:

    def __init__(self):
        self._t = dict()

    def insert(self, word: str) -> None:
        current = self._t
        for l in word:
            if l not in current:
                current[l] = dict()
            current = current[l]
        current[-1] = -1

    def search(self, word: str) -> bool:
        current = self._t
        for l in word:
            if l not in current:
                return False
            current = current[l]
        if -1 in current:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self._t
        for l in prefix:
            if l not in current:
                return False
            current = current[l]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
