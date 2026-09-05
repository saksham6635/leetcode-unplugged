class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        f = {}
        n = len(nums)
        max_freq = float('-inf')
        for i in nums:
            f[i] = f.get(i, 0) + 1
            max_freq = max(max_freq, f[i])
        res = n
        for a in f:
            if f[a] == max_freq:
                i, j = 0, n - 1
                while i < n:
                    if nums[i] == a:
                        left = i
                        break
                    i += 1
                while j >= 0:
                    if nums[j] == a:
                        right = j
                        break
                    j -= 1
                res = min(res, right - left + 1)
        return res
