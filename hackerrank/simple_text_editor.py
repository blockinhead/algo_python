class Editor:
    def __init__(self):
        super().__init__()
        self.s = []
        self.undo = []

        self.ops = {1: self.append,
                    2: self.delete,
                    3: self.prn,
                    4: self.undo_cmd}

    def apply_op(self, op):
        self.ops[op[0]](op[1])

    def append(self, w):
        self.s += list(w)
        self.undo.append((2, len(w)))

    def delete(self, k):
        k = int(k)
        self.undo.append((1, self.s[-k:]))
        del self.s[-k:]

    def prn(self, k):
        k = int(k) - 1
        print(self.s[k])

    def undo_cmd(self, arg):
        self.apply_op(self.undo.pop())
        self.undo.pop()


editor = Editor()
editor.apply_op((1, 'abc'))
editor.apply_op((3, 3))
editor.apply_op((2, 3))
editor.apply_op((1, 'xy'))
editor.apply_op((3, 2))
editor.apply_op((4, 0))
editor.apply_op((4, 0))
editor.apply_op((3, 1))
