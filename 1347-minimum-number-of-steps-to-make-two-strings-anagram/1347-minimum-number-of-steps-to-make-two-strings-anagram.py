class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c=0
        for i in set(s):
            if s.count(i)-t.count(i)>=0:
                c+=s.count(i)-t.count(i)

        return c

        
        
        