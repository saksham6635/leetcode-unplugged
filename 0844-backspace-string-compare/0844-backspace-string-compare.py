class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1,stack2=[],[]
        for i in s:
            if i.isalpha():
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
                else:
                    continue

        for i in t:
            if i.isalpha():
                stack2.append(i)
            else:
                if stack2:
                    stack2.pop()
                else:
                    continue
        return stack1==stack2

        
