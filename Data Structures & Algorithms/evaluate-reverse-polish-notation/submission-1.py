class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tmp_stack = []

        for each in tokens:
            if each not in ('+','-','*','/'):
                tmp_stack.append(each)
                continue

            last1 = int(tmp_stack.pop())
            last2 = int(tmp_stack.pop())

            if each == '+':
                tmp_stack.append(last2 + last1)

            if each == '-':
                tmp_stack.append(last2 - last1)

            if each == '*':
                tmp_stack.append(last2 * last1)

            if each == '/':
                tmp_stack.append(last2 / last1)

        return int(tmp_stack[0]) if tmp_stack else None
