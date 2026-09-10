class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n=len(s)
        count=0
        for i in range(n):
            for j in range(i+1,n+1):
                sub=s[i:j]
                if sub.count("1")<=k or sub.count("0")<=k:
                    count+=1
        return count

        