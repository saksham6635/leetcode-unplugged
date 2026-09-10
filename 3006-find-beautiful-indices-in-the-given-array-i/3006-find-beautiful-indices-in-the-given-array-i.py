class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        l,m,ans=[],[],[]
        for i in range(len(s)-len(a)+1):
            if s[i:i+len(a)]==a:
                l.append(i)
        for j in range(len(s)-len(b)+1):
            if s[j:j+len(b)]==b:
                m.append(j)
        for i in l:
            for j in m:
                if abs(i-j)<=k:
                    ans.append(i)
                    break
        return sorted(ans)


        