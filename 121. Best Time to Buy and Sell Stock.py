class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = 10001
        maxBenefit = 0

        for price in prices :
            if price < minPrice :
                minPrice = price
            if price - minPrice > maxBenefit:
                maxBenefit = price - minPrice

        return maxBenefit 
