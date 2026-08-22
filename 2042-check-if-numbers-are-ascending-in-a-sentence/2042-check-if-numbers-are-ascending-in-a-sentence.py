class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums=[]
        for i in s.split():
            if i.isdigit():
                nums.append(int(i))
        if sorted(nums)==nums and len(nums)==len(set(nums)):
            return True
        return False
        