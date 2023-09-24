class WordDictionary:

    def __init__(self):
        self._t = {}

    def addWord(self, word: str) -> None:
        current = self._t
        for l in word:
            if l not in current:
                current[l] = dict()
            current = current[l]
        current[-1] = {}

    def search(self, word: str) -> bool:
        # print(f'search: {word}')

        def dive(wrd: str, current: dict):
            # print(f'dive {wrd}')
            if not wrd:
                if -1 in current:
                    return True
                else:
                    return False

            if wrd[0] == '.':
                for k in current:
                    if dive(wrd[1:], current[k]):
                        return True
                return False
            else:
                if wrd[0] in current:
                    return dive(wrd[1:], current[wrd[0]])
                else:
                    return False

        return dive(word, self._t)

# как 208, но с рекурсивным поиском
