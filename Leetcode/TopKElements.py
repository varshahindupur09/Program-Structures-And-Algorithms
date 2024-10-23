# Leetcode 347

######################################################################################################
QUESTION
######################################################################################################

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

######################################################################################################
SOLUTION 1 (WITHOUT USING COLLECTIONS)
######################################################################################################

### USING BUBBLE SORT THIS PROB COULD BE SOVED IN nlogn but with reversing the same concept that is Top K Elements we can get to solve in O(n)

def topKElements(nums: list, k: int) -> list:
  count = {} #{1:3, 2:2, 3:1}
  freq = [ [] for i in range(len(nums)+1) ] # [ [], [], [], [], [], [], [] ]

  for n in nums:
    count[n] = 1 + count.get(n, 0)

  for n, c in count.items():
    freq[c].append(n) # [ [], [3], [2], [1], [], [], [] ]

  res = []
  for index in range(len(freq)+1, 0, -1):
      for n in freq[i]:
          res.append(n)
          if len(res) == k:
            return res


######################################################################################################
SOLUTION 2 (USING COLLECTIONS)
######################################################################################################
 from collections import Counter 

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    counter = Counter(nums)
    buckets = [0] * (n+1)

    print(counter)

    for num, freq in counter.items():
        if buckets[freq] == 0:
            buckets[freq] = [num]
        else:
            buckets[freq].append(num)

    res = []
    for i in range(n, -1, -1):
        if buckets[i] != 0:
            res.extend(buckets[i])
        if len(res) == k:
            return res

  
