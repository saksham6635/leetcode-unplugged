class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        half = n // 2
        arr = nums + nums
        prefix = [0] * (2 * n +1)
        for i in range(2 * n):
            prefix[i+1] = prefix[i] + arr[i]
        count = 0
        for i in range(n):
            left_sum = prefix[i+half] - prefix[i]
            right_sum = prefix[i+n] - prefix[i+half]
            if left_sum > right_sum:
                count += 1
        return count
