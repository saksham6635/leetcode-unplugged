class Solution:
    def sortVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        arr,result=[],[]
        for i in s:
            if i in vowels:
                arr.append(i)
        arr=sorted(arr)
        idx=0
        for i in s:
            if i in vowels:
                result.append(arr[idx])
                idx+=1
            else:
                result.append(i)
        return "".join(result)


        