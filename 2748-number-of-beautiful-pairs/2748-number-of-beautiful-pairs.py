class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                first=str(nums[i])[0]
                last=str(nums[j])[-1]
                if gcd(int(first),int(last))==1:
                    count+=1
        return count
        