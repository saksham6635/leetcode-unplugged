class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        l=[]
        ans=0
        n=len(mat)
        for i in range(len(mat)):
            a=mat[i].count(1)
            ans=max(ans,a)
        for i in range(len(mat)):
            if mat[i].count(1)==ans:
                n=min(n,i)
        l.append(n)
        l.append(ans)
        return l

        