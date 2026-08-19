class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            l.append(abs(i))
        arr=sorted(l)
        n=len(nums)
        ans=0
        left=0
        right=0       
        if n%2==0:
            arr1=arr[:n//2]
            arr2=arr[n//2:]
            for i in range(n//2):
                ans+=(arr2[i]*arr2[i])-(arr1[i]*arr1[i])
            return ans 
        elif n%2==1:
            arr1=arr[:n//2]
            arr2=arr[n//2:]
            for i in arr2:
                right+=i*i
            for i in arr1:
                left+=i*i
            return right-left




        