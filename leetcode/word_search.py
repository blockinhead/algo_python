from typing import List
from timeit import default_timer as timer

# def is_pos_good(board, pos):
#     i, j = pos
#     return 0 <= i < len(board) \
#            and 0 <= j < len(board[0])


def look_nearby(board, word, pos, visited) -> bool:
    if word == '':
        return True
    i_, j_  = pos
    # if i_ < 0 or i_ >= len(board):
    #     return False
    # if j_ < 0 or j_ >= len(board[0]):
    #     return False

    # p = pos
    # l = [(p[0], p[1] - 1),
    #      (p[0], p[1] + 1),
    #      (p[0] - 1, p[1]),
    #      (p[0] + 1, p[1])
    #      ]
    # l = [x for x in l if is_pos_good(board, x)]
    for i, j in ((i_, j_ - 1), (i_, j_ + 1), (i_ - 1, j_), (i_ + 1, j_)):
        if i < 0 or i >= len(board):
            continue
        if j < 0 or j >= len(board[0]):
            continue

        if visited[i][j]:
            continue
        if board[i][j] == word[0]:
            visited[i][j] = True
            if look_nearby(board, word[1:], (i, j), visited):
                return True
            visited[i][j] = False

    return False



def exist(self, board: List[List[str]], word: str) -> bool:

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                visited = [[False] * len(board[0]) for _ in range(len(board))]
                visited[i][j] = True
                if look_nearby(board, word[1:], (i, j), visited):
                    return True

    return False

# print(exist(None, board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
# print(exist(None, board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABF"))
# print(exist(None, board = [["A","B","C","E"],
#                            ["S","F","C","S"],
#                            ["A","D","E","E"]], word = "SEE"))
t = timer()
print(exist(None, board = [["A","A","A","A","A","A"],
                           ["A","A","A","A","A","A"],
                           ["A","A","A","A","A","A"],
                           ["A","A","A","A","A","A"],
                           ["A","A","A","A","A","A"],
                           ["A","A","A","A","A","A"]],
            word = "AAAAAAAAAAAAAAa"))
print(timer() - t)

t = timer()
print(exist(None, board =[["A","B","C","E"],
                          ["S","F","E","S"],
                          ["A","D","E","E"]],
                  word = "ABCESEEEFS"))

print(timer() - t)

