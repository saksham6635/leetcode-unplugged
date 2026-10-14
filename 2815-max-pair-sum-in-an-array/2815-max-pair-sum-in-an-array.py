class Solution:
    def maxSum(self, nums: List[int]) -> int:
        groups = {}
        for num in nums:
            max_digit = max(int(d) for d in str(num))
            if max_digit not in groups:
                groups[max_digit] = []
            groups[max_digit].append(num)
        
        ans = -1
        for vals in groups.values():
            if len(vals) >= 2:
                vals.sort(reverse=True)
                ans = max(ans, vals[0] + vals[1])
        return ans
