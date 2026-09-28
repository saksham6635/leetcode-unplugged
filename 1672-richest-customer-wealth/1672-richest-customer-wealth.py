class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans=0
        for i in accounts:
            amount=sum(i)
            ans=max(ans,amount)
        return ans 
        