# A string S of lowercase English letters is given. We want to partition this 
# string into as many parts as possible so that each letter appears in at 
# most one part, and return a list of integers representing the size of these parts.
# 
# Example:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
# because it splits S into less parts.

class Solution:
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        return enumerate(S)


# Solution:
S = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(S))

