link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

##################################################################
solution:
##################################################################

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # trying sliding window 
        i, j, max_sum, hashset, curr_sum = 0, 0, 0, set(), 0

        while j < len(nums):
            # expand window
            if nums[j] not in hashset:
                hashset.add(nums[j])
                curr_sum += nums[j]
                j += 1

                # window size
                if j-i == k:
                    max_sum = max(max_sum, curr_sum)
                    hashset.remove(nums[i])
                    curr_sum -= nums[i]
                    i += 1
            else:
                # duplicate
                hashset.remove(nums[i])
                curr_sum -= nums[i]
                i += 1

        return max_sum
                
                
