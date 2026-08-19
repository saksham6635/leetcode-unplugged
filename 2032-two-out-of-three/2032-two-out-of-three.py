class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr=[]
        nums4=nums1+nums2+nums3
        for i in set(nums4):
            if i in nums1 and i in nums2:
                arr.append(i)
            elif i in nums2 and i in nums3:
                arr.append(i)
            elif i in nums1 and i in nums3:
                arr.append(i)
        return list(set(arr))



        