class Solution:
    def isPalindrome(self, s:str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(solution.isPalindrome("race a car"))  # Output: False
    print(solution.isPalindrome(""))  # Output: True    