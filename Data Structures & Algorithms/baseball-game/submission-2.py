class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for i in operations:
            if i=='C':
                stack.pop()
            elif i == "+":
                stack.append(sum(stack[-2:]))
            elif i=='D':
                stack.append(2*stack[-1])
            else:
                stack.append(int(i))
        return sum(stack)
        