class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max([sum(x) for x in accounts])
        