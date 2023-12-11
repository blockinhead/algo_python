class Solution:
    def longestValidParentheses(self, s: str) -> int:
        d = []
        res = 0
        start = 0

        for i, p in enumerate(s):
            if p == '(':
                d.append(i)
            else:
                if d:
                    d.pop()
                    if not d:
                        res = max(res, i - start + 1)
                    else:
                        res = max(res, i - d[-1])
                else:
                    start = i + 1

        return res

# если закрыли открытую скобку, то это валидная последовательность. она начинается либо в нуле (старте), либо такм, где была предыдущая открывающая скобка, которая не закрыта
# закрывающая скобка при пустом стеке - что-то не валидное, двигаем старт. если до неё было что-то хорошее, оно посчиталось по предыдущему правилу
