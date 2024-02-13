class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        k=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=max(candies)):
                k.append(True)
            else:
                k.append(False)
        return k
        