class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        n=len(nums)
        count1,count2=0,0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    count1+=1
        arr=nums[::-1]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==target:
                    count2+=1
        return count1+count2
        

                    
        