class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        f={}
        seen=set(arr)
        freq=set()
        for i in arr:
            f[i]=f.get(i,0)+1
        for i in f:
            freq.add(f[i])
        return len(seen)==len(freq)
        
            
        
            