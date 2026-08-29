class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        #a=2^0,b=2^1...................z=2^25
        z=2**25
        ans=[]
        for num in nums:
            if num==0:
                ans.append("")
                continue
            s=""
            while num>=z:
                num-=z
                s+="z"
            while num>0:
                power=num.bit_length()-1
                word=chr(97+power)
                s+=word
                num-=2**power
            ans.append(s)
        return ans


        