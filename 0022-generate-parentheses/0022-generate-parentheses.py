class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        result=[]
        def backtrack(copen,cclose):
            if copen==cclose==n:
                result.append("".join(stack))
                return 
            if copen<n:
                stack.append("(")
                backtrack(copen+1,cclose)
                stack.pop()
            if cclose<copen:
                stack.append(")")
                backtrack(copen,cclose+1)
                stack.pop()
        backtrack(0,0)
        return result        