class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        balance=0
        for i in s:
            if i=="(":
                if balance>0:
                    stack.append(i)
                balance+=1
            else:
                balance-=1
                if balance>0:
                    stack.append(i)
        return "".join(stack)


        