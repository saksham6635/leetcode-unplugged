class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l,m=[],[]
        for i in grid:
            for j in i:
                l.append(j)
        for i in l:
            if l.count(i)==2:
                m.append(i)
                break
        for i in range(1,len(l)+1):
            if i not in l:
                m.append(i)
                break
        return m
        
                
        