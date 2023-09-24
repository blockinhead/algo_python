counter = 0

'''
with open('input') as f:
    for l in f:
        right_part = l.strip().split('|')[1]
        tokens = right_part.split()
        for t in tokens:
            if len(t) in (2, 4, 3, 7):
                counter += 1

print(counter)
'''

# top = set()
# middle = set()
# bottom = set()
# top_left = set()
# top_right = set()
# bottom_left = set()
# bottom_right = set()


with open('input') as f:
    s = 0
    for l in f:
        left_part, right_part = l.strip().split('|')
        tokens = right_part.split() + left_part.split()

        by_len = {len(t): t for t in tokens}
        top = set(by_len[3]) - set(by_len[2])
        topleft_middle = set(by_len[4]) - set(by_len[2])
        bottomleft_bottom = set(by_len[7]) - set(by_len[4]) - top
        right = set(by_len[2])
        print(f'{top=} {by_len[2]=} {by_len[3]}')

        current_s = ''
        for t in right_part.split():
            d = 0
            if len(t) == 6:  # 0, 6, 9
                if len(bottomleft_bottom - set(t)) == 0 and len(topleft_middle - set(t)) == 1:
                    d = 0
                elif len(bottomleft_bottom - set(t)) == 1 and len(topleft_middle - set(t)) == 0:
                    d = 9
                else:
                    d = 6
            elif len(t) == 5:  # 2, 3, 5
                if len(right - set(t)) == 0:
                    d = 3
                elif len(bottomleft_bottom -set(t)) == 0 and len(topleft_middle - set(t)) == 1:
                    d = 2
                else:
                    d = 5
            elif len(t) == 2:
                d = 1
            elif len(t) == 3:
                d = 7
            elif len(t) == 4:
                d = 4
            else:
                d = 8

            current_s += str(d)

        s += int(current_s)


print(s)





