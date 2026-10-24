class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        cnt = [0] * 10
        ans = 0

        for num in nums:
            last = num % 10

            for first in range(1, 10):
                if gcd(first, last) == 1:
                    ans += cnt[first]

            while num >= 10:
                num //= 10
            first_digit = num

            cnt[first_digit] += 1

        return ans