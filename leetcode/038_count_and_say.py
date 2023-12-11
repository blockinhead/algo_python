class Solution:
    def countAndSay(self, n: int) -> str:

        def parse(current_str):
            counter = 0
            prev_c = current_str[0]
            parsed = []
            for c in current_str:
                if c == prev_c:
                    counter += 1
                else:
                    parsed.append(f'{counter}{prev_c}')
                    counter = 1
                    prev_c = c
            parsed.append(f'{counter}{prev_c}')
            # print(f'{current_str=} {parsed=}')

            return ''.join(parsed)

        c = '1'
        for _ in range(n - 1):
            c = parse(c)

        return c
