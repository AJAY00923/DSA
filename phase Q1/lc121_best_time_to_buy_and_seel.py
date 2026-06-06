class Solution:
    def maxProfit(self, Prices: list(int)) -> int:
        if not Prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0  

        for price in Prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price  
        return max_profit   
    
# Example usage:
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))  # Output: 0
