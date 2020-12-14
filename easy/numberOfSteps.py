#vGiven a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, n):
        nSteps = 0
        while n > 0:
            if not n%2:
                nSteps += 1
                n /= 2
            else:
                n -= 1
                nSteps += 1
        return nSteps

solution = Solution()
print(solution.numberOfSteps(14))
                


