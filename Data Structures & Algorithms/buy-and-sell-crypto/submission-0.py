# 10 5 20
# 10 15 20
# 10 9 8




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max_profit = sell - buy # 0
        for curr_day_price in prices:
            curr_profit = curr_day_price - buy # sell at curr day
            if curr_profit > max_profit:
                max_profit = curr_profit

            if curr_day_price < buy:
                buy = curr_day_price # buy at curr day 
        
        return max_profit       
            



            
        