class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            return self.addBinary(b, a)

        s = {('1', '1'): ('0', '1'),
             ('1', '0'): ('1', '0'),
             ('0', '1'): ('1', '0'),
             ('0', '0'): ('0', '0')
        }

        res = []
        flag = '0'
        for i in range(1, len(a) + 1):
            tmp_v, new_flag1 = s[(a[-i], b[-i])]
            v, new_flag2 = s[(tmp_v, flag)]
            flag, _ = s[(new_flag1, new_flag2)]
            # print(f'{a[-i]=} {b[-i]=} {v=} {flag=}')
            res.append(v)

        for i in range(len(a) + 1, len(b) + 1):
            tmp_v, new_flag1 = s[('0', b[-i])]
            v, new_flag2 = s[(tmp_v, flag)]
            flag, _ = s[(new_flag1, new_flag2)]
            # print(f'{b[-i]=} {v=} {flag=}')
            res.append(v)
        if flag == '1':
            res.append(flag)

        return ''.join(reversed(res))
