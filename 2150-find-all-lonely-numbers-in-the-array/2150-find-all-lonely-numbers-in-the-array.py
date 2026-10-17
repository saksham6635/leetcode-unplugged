class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        seen = set(nums)
        rem = dict()
        for n in nums:
            if (n-1) in seen or (n+1) in seen:
                continue
            rem[n] = rem.get(n,0) +1

        return [r for r in rem if rem[r] ==1] 