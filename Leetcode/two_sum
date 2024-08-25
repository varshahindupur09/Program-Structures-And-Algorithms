
# leetcode two sum

# solution with one for/while loop

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = nums[i] 
            y = target - x 
            lis = nums[i+1:]
            if y in lis:
                ind = lis.index(y)+ (len(nums)-len(lis))
                return [i,ind]

# this uniquely uses a logic to fetch index instead of a loop

# solution using DS
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashm:
                return [hashm[diff],i]
            hashm[n] = i
