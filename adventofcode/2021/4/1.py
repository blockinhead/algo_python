class Board(object):
    def __init__(self, rows):
        self.board = []  # type: list[list]
        self.mask = []
        for _ in range(5):
            self.mask.append([0] * 5)

        for r in rows:
            self.board.append(r[:])

        self.won = False

    def check(self, x):
        for r, row in enumerate(self.board):
            for i in range(len(row)):
                if row[i] == x:
                    self.mask[r][i] = 1

        for r in range(len(self.mask)):
            if sum(self.mask[r]) == len(self.mask[r]):
                return self.sum_unmarked() * x

        mask_columns = zip(*self.mask)
        for c, col in enumerate(mask_columns):
            if sum(col) == len(self.board):
                return self.sum_unmarked() * x

        return 0

    def sum_unmarked(self):
        acc = 0
        for r in range(len(self.mask)):
            for c in range(len(self.mask[r])):
                if not self.mask[r][c]:
                    acc += self.board[r][c]
        return acc


with open('input') as f:
    digits = [int(x) for x in f.readline().strip().split(',')]

    boards = []

    accum = []
    while line := f.readline():
        line = line.strip()
        if line:
            accum.append([int(x) for x in line.split()])
        if len(accum) == 5:
            boards.append(Board(accum))
            accum = []

    for d in digits:
        for b in boards:
            if b.won:
                continue
            if res := b.check(d):
                b.won = True
                print(res)



