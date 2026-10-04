class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        n = len(nums)
        key_indices = [i for i, val in enumerate(nums) if val == key]        
        res = []
        j = 0          
        for i in range(n):           
            while j < len(key_indices) and key_indices[j] < i - k:
                j += 1
            if j < len(key_indices) and abs(i - key_indices[j]) <= k:
                res.append(i)
        
        return res
