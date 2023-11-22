from string import ascii_lowercase
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = dict()

        for product in products:
            level = trie
            for l in product:
                if l not in level:
                    level[l] = dict()
                level = level[l]
            level['*'] = product

        def get_words(some_level):
            words = []

            def dive(lev):
                if len(words) == 3:
                    return

                if '*' in lev:
                    words.append(lev['*'])
                for l in ascii_lowercase:
                    if l not in lev:
                        continue
                    dive(lev[l])

            dive(some_level)
            return words

        res = []
        level = trie
        for l in searchWord:
            if not level or l not in level:
                res.append([])
                level = None  # как только буква не нашлась в трае, дальше должны быть пустые ответы. если не присвоить тут нан, то алгоритм перепрыгнет на следующую букву
                continue
            level = level[l]

            res.append(get_words(level))

        return res


print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], 'mouse'))

# бинарный поиск был бы быстрее
# сортим продуктс
# берём кусок слова от начала до текущей бувы и бинарно ищем по startswith место вставки
# от этого места берём максимум три следующих слова
