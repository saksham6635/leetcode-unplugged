class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops=0
        seen=set()
        for i in nums[::-1]:
            ops+=1
            if i<=k:
                seen.add(i)
            if len(seen)==k:
                return ops
        return ops 
            

        