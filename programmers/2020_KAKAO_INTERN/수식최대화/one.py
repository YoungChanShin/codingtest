from itertools import permutations
import re


def solution(expression):
    answer = 0
    expression = re.split("([-+*])", expression)

    def calculate(priority):
        nonlocal expression
        ex = expression[:]
        stack = ex[:]
        num1 = float("inf")
        for i in range(3):
            op = priority[i]
            ex = stack[:]
            stack = []
            # print(ex)
            for e in ex:
                if num1 != float("inf"):
                    stack.append(str(eval(num1 + op + e)))
                    num1 = float("inf")
                    continue
                if e == op:
                    num1 = stack.pop()
                    continue
                stack.append(e)
        # print(stack)
        return int(stack[0])

    for priority in permutations(["+", "-", "*"]):
        answer = max(answer, abs(calculate(priority)))

    return answer


e = "100-200*300-500+20"
print(solution(e))