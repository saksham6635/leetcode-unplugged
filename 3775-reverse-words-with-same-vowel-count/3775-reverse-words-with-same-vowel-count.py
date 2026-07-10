class Solution:
    def reverseWords(self, s: str) -> str:
        stack=s.split()
        freq={x:x.count("a")+x.count("e")+x.count("i")+x.count("o")+x.count("u") for x in stack}
        n=len(stack)
        for i in range(1,n):
            if freq[stack[0]]==freq[stack[i]]:
                stack[i]=stack[i][::-1]
        new_string=" ".join(map(str,stack))
        return new_string
        