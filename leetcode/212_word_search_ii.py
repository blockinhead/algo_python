from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tri = {}
        for w in words:
            current_d = tri
            for l in w:
                if l not in current_d:
                    current_d[l] = {}
                current_d = current_d[l]
            current_d['$'] = w  # в признак конца слова положу само слово, так не нужно будет его собирать в поиске

        res = set()

        def dive(current_d, row, col):
            if '$' in current_d:
                res.add(current_d['$'])
                # если найденное слово удалить из трая, то будет быстрее, мы не будем его больше искать

            if not (0 <= row < len(board)) or not (0 <= col < len(board[0])):
                return

            ch = board[row][col]
            if ch not in current_d:
                return

            board[row][col] = '.'
            dive(current_d[ch], row + 1, col)
            dive(current_d[ch], row - 1, col)
            dive(current_d[ch], row, col + 1)
            dive(current_d[ch], row, col - 1)
            board[row][col] = ch

        for row in range(len(board)):
            for col in range(len(board[0])):
                dive(tri, row, col)

        return list(res)
