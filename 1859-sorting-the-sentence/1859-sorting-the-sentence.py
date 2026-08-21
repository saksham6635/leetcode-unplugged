class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        l,m=[],[]
        for i in s:
            l.append(i[-1]+i[:-1])
        for i in sorted(l):
            m.append(i[1:])
        ans=" ".join(m)
        return ans 
