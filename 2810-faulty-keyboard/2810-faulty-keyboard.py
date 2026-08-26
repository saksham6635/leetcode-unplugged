class Solution:
    def finalString(self, s: str) -> str:
        new_string=""
        for i in s:
            new_string+=i
            if i=="i":
                new_string=new_string[::-1]
        result=new_string.replace("i","")
        return result
        