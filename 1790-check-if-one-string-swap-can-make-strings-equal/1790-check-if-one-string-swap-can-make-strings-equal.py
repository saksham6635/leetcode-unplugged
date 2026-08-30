class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        count=0
        d1,d2={},{}
        for i in s1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in s2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        if d1!=d2:
            return False
        else:
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
        if count==0 or count==2:
            return True
        return False

        