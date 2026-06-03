"""Longest Substring Without Repeating Characters"""
class Solution:
    def lengthofLongestSubstring(self, s:str) -> int:
        seen = {}
        left =0
        max_count = 0
        for right, char in enumerate(s):
            if char in seen and seen[char]>=1 :
                left = seen[char]+1
            seen[char] = right
            max_count = max(max_count, right-left+1 )
        return max_count
    
s = Solution()
print(s.lengthofLongestSubstring("abcabcbb"))  # 3
print(s.lengthofLongestSubstring("bbbbb"))     # 1
print(s.lengthofLongestSubstring("pwwkew"))     # 3