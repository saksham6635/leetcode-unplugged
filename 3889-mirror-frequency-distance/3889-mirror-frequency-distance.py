class Solution:
    def mirrorFrequency(self, s: str) -> int:
        ans = 0

        while s:
            i = s[0]

            if i.isdigit():
                mirror = str(9 - int(i))
            else:
                mirror = chr(219 - ord(i))  

            c = s.count(i)
            m = s.count(mirror)

            ans += abs(c - m)

            s = s.replace(i, "")

            if mirror != i:
                s = s.replace(mirror, "")

        return ans