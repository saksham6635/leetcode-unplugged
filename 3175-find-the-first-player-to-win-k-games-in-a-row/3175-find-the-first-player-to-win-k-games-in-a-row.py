class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n=len(skills)
        k=min(k,n-1)
        w=0
        conseq=0
        for i in range(1,n):
            if skills[w]<skills[i]:
                conseq=1
                w=i
            else:
                conseq+=1
            if conseq==k:
                break
        return w        