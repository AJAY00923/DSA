class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        position = 0 # position to fill the rest of the numbers
        for num in nums:# goes through each number of numbers list
            if num!=0:# it checks weather its zero or regular and if it is not zero 
                nums[position] = num# then the number is going to add to the posiiton
                position +=1 # and the position is increased by 1
        
            
        while position < len(nums):# after filling all non zero numbers checks if its is still len than the actual nums when it is
            nums[position] = 0# its gonna fill the rest with 0
            position +=1# until it reach len nums
# Time complexity is O(n) because we are going through the list once and then filling the rest with zeroes
# Space complexity is O(1) because we are modifying the list in place and not using
# any extra space.  
solution = Solution()
nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)