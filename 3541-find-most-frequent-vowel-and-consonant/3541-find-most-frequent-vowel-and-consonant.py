class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={'a', 'e', 'i', 'o', 'u'}
        freq={}
        l,m=[],[]
        for i in s:
            if i in d:
                freq[i]=freq.get(i,0)+1
                l.append(freq[i])
            else:
                freq[i]=freq.get(i,0)+1
                m.append(freq[i])
        if len(l)>0 and len(m)>0:
            return max(l)+max(m)
        elif len(l)==0 and len(m)>0:
            return max(m)
        elif len(l)>0 and len(m)==0:
            return max(l)
        else:
            return 0
        
            
        