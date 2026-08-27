class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        output,val=0,0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(0)
            elif i==")":
                mul=stack.pop()
                if mul==0:
                    val=1
                else:
                    val=mul*2
                if not stack:
                    output+=val
                else:
                    stack[-1]+=val
        return output

        