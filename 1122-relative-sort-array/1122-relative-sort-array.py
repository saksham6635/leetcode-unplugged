class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq={}
        l,m=[],[]
        for i in arr1:
            freq[i]=freq.get(i,0)+1
            if i not in arr2:
                m.append(i)
        for i in arr2:
            if i in freq:
                l.extend([i]*freq[i])
        return l+sorted(m)
        


        