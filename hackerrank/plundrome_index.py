def palindromeIndex(s):
    # Write your code here
    if len(s) == 1 and len(s) == 2:
        return -1

    start = 0
    end = len(s) - 1

    to_remove = -1

    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
            continue

        if to_remove != -1:
            return -1

        if s[start + 1] == s[end]:
            to_remove = start
            start += 1
        elif s[start] == s[end - 1]:
            to_remove = end
            end -= 1

    print('all_good?')
    return to_remove


# print(palindromeIndex('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'))
print(palindromeIndex('fcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwf'))
# print(palindromeIndex('fcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcf'))
