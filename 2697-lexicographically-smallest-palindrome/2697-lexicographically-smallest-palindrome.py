class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        arr = list(s)
        i, j = 0, len(arr) - 1

        while i < j:
            if arr[i] != arr[j]:
                if arr[i] > arr[j]:
                    arr[i] = arr[j]
                else:
                    arr[j] = arr[i]
            i += 1
            j -= 1

        return "".join(arr)

            
        
        

        