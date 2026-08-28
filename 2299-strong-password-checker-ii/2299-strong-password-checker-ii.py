class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lower,upper,digit=0,0,0
        a=0
        special="!@#$%^&*()-+"
        if len(password)<8:
            return False
        for ch in password:
            if ch.isdigit():
                digit=1
            elif ch.isupper():
                upper=1
            elif ch.islower():
                lower=1
            elif ch in special:
                a=1
        for i in range(1,len(password)):
            if password[i]==password[i-1]:
                return False
        return a+upper+lower+digit==4
        
        
        
        
            
        
        
        
        