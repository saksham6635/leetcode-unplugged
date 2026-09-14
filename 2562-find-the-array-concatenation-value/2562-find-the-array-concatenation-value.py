class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        c = 0
        while i <= j:
            if i == j:
                c += nums[i]  
            else:
                c += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1

        return c
