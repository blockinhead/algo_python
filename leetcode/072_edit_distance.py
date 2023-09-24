class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            # эдит дистанс от пустой строки до подстроки word2[:j + 1]
            d[0][j] = j

        for i in range(len(word1) + 1):
            d[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # эдит дистанс от строки word1[:i] до строки word2[:j]
                # если последние буквы этих слов одинаковые, то эдит дистанс у них такой же,
                # как у слов на одну букву короче
                # если разный - то мы можем либо добавить букву, удалить букву, или поменять букву
                # поменять - это значит эдит дистанс будет такой же, как у слов на одну букву короче, + 1
                # добавить - это значит эдит дистанс будет такой же, как у word1[:i-1] и word2[:j], + 1
                # удалить - это значит эдит дистанс будет такой же, как у word1[:i] и word2[:j-1], + 1
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i][j - 1], d[i - 1][j - 1], d[i - 1][j]) + 1

        # for s in d:
        # print(s)

        return d[-1][-1]
