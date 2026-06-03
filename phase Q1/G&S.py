def min_max(nums):
    return(min(nums), max(nums))

lo, hi = min_max([1,2,3,4])
print(lo,hi)
from collections import defaultdict
# Collections . defaultdict
"""A dictionary that never throws KeyError - give a default value automatically"""
# Normal dict - crashes
# d = {}
# d['a'] += 1    # KeyEroor! 'a' doesn't exist yet

# defaultdict - never crashes
d = defaultdict(int) # default value is 0
d['a'] +=1           # works -> d['a'] = 1
d['b'] +=1           # works -> d['b'] = 1

# default of list - grooup items
groups = defaultdict(list)
groups['vowels'].append('a') # no Key error
groups['vowels'].append('e')
groups['consonants'].append('b')
print(groups)

# Collections.Counter

from collections import Counter

words = ['Apple', 'banana', 'Apple', 'cherry', 'banana', 'Apple']
count = Counter(words)

print(count['Apple'])

print(Counter('hello'))

c1 = Counter('aab')
c2 = Counter('ab')
print(c1-c2)



# Deque (double-ended queue)
"""A list that is O(1) at BOTH ends - front and back 
                Regular list is O(n) at the front"""
from collections import deque

q = deque()
q.append(1) # add to right -> O(1)
q.append(2)
q.appendleft(0) # add to left -> )O(1)
q.pop() # remove right -> O(1)
q.popleft()  # remove left -> O(1) This is why we use deque not listed

# Use as a queue (FIFO)
queue = deque([1,2, 3])
print(queue.append(4)) # enqueue
print(queue.popleft()) # deqeue -> 1
print(queue)
"""When to use: BFS traversal, sliding window maximum, anything needing fast front removal"""
"""Need ordered data with index access?  → List
Need key-value lookup?                → Dictionary
Need "have I seen this?" fast?        → Set
Need immutable pair/coordinate?       → Tuple
Need counting without KeyError?       → Counter
Need grouping without KeyError?       → defaultdict
Need fast add/remove from both ends?  → Deque
"""
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_freq = {}
for word in words:
        word_freq[word]=word_freq.get(word,0) +1
print(word_freq)
# Expected output:
# {"apple": 3, "banana": 2, "cherry": 1}

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Remove duplicates but preserve original order
# Expected: [3, 1, 4, 5, 9, 2, 6]
print(list(set(nums)))
seen = set()
result = []
for num in nums:
    if num not in seen:
        result.append(num)
        seen.add(num)
print(result)
            
## BIG o noataion 
"""How does my code slow down as input gets bigger
The 4 you need for GS
O(1) — Constant
Input size doesn't matter. Always the same speed.
python"""
def get_first(nums):
    return nums[0]   # always 1 operation, wheather n =10 or n = 10^10

d = {'a': 1, 'b': 2}
d['a']                  # always 1 operation — hash lookup

"""O(n) — Linear
One loop through input. Double the input → double the work."""

def find_max(nums):
    max_val = float('-inf')
    for num in nums:
        if num > max_val:
             max_val = num
    
    return max_val

print(find_max([2, 3, 4, 5, 7, 5 ]))

"""O(n²) — Quadratic
Loop inside a loop. Double the input → 4x the work. Dangerous for large inputs."""
def has_duplicate(nums):
     for i in range(len(nums)):
          for j in range(i+1, len(nums)):
               if nums[i] == nums[j]:
                    return True
    
     return False  

"""O(log n) — Logarithmic
Input gets cut in half each step. Extremely fast. Appears in binary search and balanced trees."""
def binary_Search(nums, target):
     left, right = 0, len(nums) - 1
     while left <= right:
          mid = (left + right) // 2
          if nums[mid] < target:
               left = mid + 1
          else:
               right = mid - 1
     return -1

print(binary_Search([1, 2, 4, 5,  43, 77, 67, 87, ], 5))
"""How to calculate complexity by looking at code
One loop           → O(n)
Two nested loops   → O(n²)
Loop that halves   → O(log n)
No loop            → O(1)
Loop + inner loop that halves → O(n log n)  ← sorting"""
# checking palindrom
def is_palindrome(s):
     #clean the string first
     s = ''.join(char.lower()for char in s if char.isalnum())
     left = 0
     right = len(s) - 1

     while left < right:
          if s[left] != s[right]:
               return False
          left +=1
          right -=1

     return True

# nums = [2, 7, 11, 15],  target = 9
# # Output: [1, 2]   #(1-based: position 1 and position 2)

# nums = [2, 3, 4],  target = 6
# # Output: [1, 3]

# nums = [-1, 0],  target = -1
# Output: [1, 2]
def two_sums(nums, target):
     left = 0
     right = len(nums) - 1

     while left < right:
          current_sum = nums[left] + nums[right]

          if current_sum == target:
               return [left + 1, right + 1]
          elif current_sum < target:
               left +=1
          else:
               right -=1
     return []

nums = [2, 3, 4]
target = 6
print(two_sums(nums, target))
"""PHASE 1 — Step 4: SLIDING WINDOW PATTERN
1.Fixed window — size never changes
"Find max sum subarray of size k"
2.Variable window — size grows and shrinks
"Find longest substring without repeating characters"
"""
def max_sum_subarray(nums, k):#Fixed window
     #Build First Window
     window_sum = sum(nums[:k])
     max_sum = window_sum

     #Slide forward - add right element , remove left element
     for i in range(k , len(nums)):
          window_sum += nums[i]
          window_sum +=nums[i-k]
          max_sum = max(max_sum, window_sum)

     return max_sum 

def length_of_longest_substring(s):
     seen = set()
     left = 0
     max_len = 0
     # shrink window from until no duplicates
     for right in range(len(s)):
          while s[right] in seen:
               seen.remove(s[left])
               left +=1
          seen.add(s[right])
          max_len=(max(max_len, right - left + 1))
     return max_len

def max_avg_subarray(nums, k):
    window_sum = sum(nums[:k])      # this is a SUM, call it sum
    max_avg = window_sum / k        # first average

    for i in range(k, len(nums)):
        window_sum += nums[i]       # add incoming element to SUM
        window_sum -= nums[i - k]   # remove outgoing element from SUM
        max_avg = max(max_avg, window_sum / k)  # divide SUM by k = average

    return max_avg

def first_missing_positive(nums):
    num_set = set(nums)        # O(n) to build, O(1) to lookup

    i = 1
    while i <= len(nums) + 1:         # what's the condition to keep checking?
        if i not in num_set:
            return i
        i += 1
print(first_missing_positive([3, 4, -1, 1]))  # 2
print(first_missing_positive([1, 2, 0]))       # 3
print(first_missing_positive([7, 8, 9]))       # 1