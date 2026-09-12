class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zero=nums.count(0)
        arr1=[0]*zero
        arr2=nums[-zero:]
        count=0
        for i in range(len(arr1)):
            if arr2[i]!=arr1[i]:
                count+=1
        return count



     
        