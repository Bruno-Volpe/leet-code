class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        can_buy = True
        bought = 0
        sold = 0
        
        for i in range(len(prices)):
            if i == len(prices) - 1:
                if not can_buy:
                    sold += prices[i] - bought
                    bought = 0
                    can_buy = True
                break
            
            if prices[i+1] > prices[i] and can_buy:
                bought = prices[i]
                can_buy = False
            
            if prices[i+1] < prices[i] and not can_buy:
                sold += prices[i] - bought
                bought = 0
                can_buy = True
                
            
        return sold
                