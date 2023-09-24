class Solution:
    def convert(self, s: str, numRows: int) -> str:

        columns = []
        i = 0
        while i < len(s):
            columns.append([' '] * numRows)
            for j in range(numRows):
                if i == len(s):
                    break
                columns[-1][j] = s[i]
                i += 1
            for j in range(1, numRows - 1):
                if i == len(s):
                    break
                columns.append([' '] * numRows)
                columns[-1][-j - 1] = s[i]
                i += 1

        res = ''
        for l in zip(*columns):
            print(l)
            res += ''.join([x for x in l if x != ' '])

        return res

    
print(Solution().convert('PAYPALISHIRING', 4))
