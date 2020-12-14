import random

class Solution:

    def pythonicPiEstimator(self,nIterations):
        # Using List Comprehesion:
        totalInside = sum([self.isInside(random.random(),random.random()) for iteration in range(nIterations)])
        return 4*totalInside/nIterations

    def piEstimation(self,nIterations):
        points = []
        for point in range(nIterations):
            xCor, yCor = random.random(), random.random()
            points.append(self.isInside(xCor,yCor))
        totalInside = sum(points)
        pi = 4*totalInside/nIterations
        return pi
    
    def isInside(self,xCor,yCor):
        return int(xCor**2 + yCor**2 <= 1)

solution = Solution()
print(solution.piEstimation(1000000000))

