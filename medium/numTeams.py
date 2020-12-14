# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
# You have to form a team of 3 soldiers amongst them under the following rules:
# 
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) 
# or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
# 
# EXAMPLE:
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 


class Solution:
    # SOLUCION FUERZA BRUTA
    def numTeams(self, ratings):
        
        nTeams = 0

        for i in range(len(ratings)):
            firstTeamMember = ratings[i]

            for j in range(i+1, len(ratings)):
                secondTeamMember = ratings[j]

                if firstTeamMember > secondTeamMember:
                    isHigher = True
                else:
                    isHigher = False

                for k in range(j+1, len(ratings)):
                    thirdTeamMember = ratings[k]
                    if secondTeamMember > thirdTeamMember:
                        isAlsoHigher = True
                    else:
                        isAlsoHigher = False

                    if isHigher == isAlsoHigher:
                        nTeams += 1
        return nTeams

solution = Solution()
ratings = [1,2,3,4]
print(solution.numTeams(ratings))
                


