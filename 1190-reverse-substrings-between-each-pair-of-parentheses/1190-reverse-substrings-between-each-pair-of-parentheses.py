class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i==")":
                t=[]
                while stack and stack[-1]!="(":
                    t.append(stack.pop())
                stack.pop()
                stack.extend(t)
            else:
                stack.append(i)
        return "".join(stack)