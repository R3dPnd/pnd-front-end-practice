class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0

        paths = [n]

        while paths:
            curr = paths.pop()
            if curr == 0:
                count += 1
                continue
            if curr < 0:
                continue
            paths.append(curr -1)
            paths.append(curr -2)

        return count