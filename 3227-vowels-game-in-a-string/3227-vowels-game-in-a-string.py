class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels={"a","e","i","o","u"}
        count=0
        for i in s:
            if i in vowels:
                count+=1
        if count==0:
            return False
        if count%2==1:
            return True
        if count%2==0:
            return True
        
       