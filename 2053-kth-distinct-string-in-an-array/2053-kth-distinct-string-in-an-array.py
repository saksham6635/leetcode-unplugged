class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        distinct=[]
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i]==1:
                distinct.append(i)
        if len(distinct)<k:
            return ""
        return distinct[k-1]

        