def two_sum(nums, target):
    n = len(nums)
    for num1 in range(0, n):
        for num2 in range(num1+1, n):
            if nums[num1]+nums[num2]==target:
                return [num1, num2]
print("=== Two Sum ===")
print(two_sum([2, 7, 11, 15], 9))   # expect [0, 1]
print(two_sum([3, 2, 4], 6))         # expect [1, 2]
print(two_sum([3, 3], 6))            # expect [0, 1]

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        else:
            profit = i - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit
print("\n=== Max Profit ===")
print(max_profit([7, 1, 5, 3, 6, 4]))  # expect 5
print(max_profit([7, 6, 4, 3, 1]))      # expect 0
print(max_profit([1]))                   # expect 0
print(max_profit([2, 6, 1, 3])) 