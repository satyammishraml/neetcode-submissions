class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            print("i", i)
            if i=='C':
                stack.pop()
            elif i not in ['C', 'D', '+']:
                stack.append(int(i))
            elif i == "+":
                stack.append(sum(stack[-2:]))
            elif i=='D':
                stack.append(2*stack[-1])
            print(stack)
        print(stack)
        return sum(stack)
        