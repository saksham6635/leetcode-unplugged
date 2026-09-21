class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        seen=set(nums1).intersection(set(nums2))
        if len(seen)>0:
            l=list(seen)
            return min(l)
        a=str(min(nums1))
        b=str(min(nums2))
        c=int(a+b)
        d=int(b+a)
        return min(c,d)
