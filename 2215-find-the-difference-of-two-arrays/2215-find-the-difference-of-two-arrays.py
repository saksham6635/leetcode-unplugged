class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l,m,res=[],[],[]
        for i in set(nums1):
            if i not in set(nums2):
                l.append(i)
        for i in set(nums2):
            if i not in set(nums1):
                m.append(i)
        res.append(l)
        res.append(m)
        return res

        