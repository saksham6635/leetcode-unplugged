class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        l=[]
        ans=0
        for i in set(s):
            l.append(s.count(i))
        freq=sorted(l)
        n=len(freq)
        if n<=k:
            return 0
        elif n>k:
            return sum(freq[:n-k])

            



        