class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        alice = [0] * 366
        bob = [0] * 366

        year = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Alice
        a = int(arriveAlice[:2])
        b = int(arriveAlice[3:])
        c = int(leaveAlice[:2])
        d = int(leaveAlice[3:])

        startA = sum(year[:a]) + b
        endA = sum(year[:c]) + d

        for i in range(startA, endA + 1):
            alice[i] = 1

        # Bob
        p = int(arriveBob[:2])
        q = int(arriveBob[3:])
        r = int(leaveBob[:2])
        s = int(leaveBob[3:])

        startB = sum(year[:p]) + q
        endB = sum(year[:r]) + s

        for i in range(startB, endB + 1):
            bob[i] = 1

        ans = 0
        for i in range(366):
            if alice[i] == 1 and bob[i] == 1:
                ans += 1

        return ans