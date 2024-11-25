# Imagine an algorithm that iterates through n elements and for each element 
# performs a binary search on a separate data structure of size k. This would 
# likely have a time complexity of O(n log k) because the binary search operation 
# takes O(log k) time.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # without sorting -> min heap (priority queue)
        # minheap = [(x * -1) for x in nums[:k]] #2,3 #5,3=>3,5 #6,5=>5,6
        # minheap = nums[:k]
        # heapq.heapify(minheap)
        # print(minheap)
        
        # for num in nums[k:]:
        #     if num > minheap[0]:
        #         heapq.heapreplace(minheap, num)
        # return minheap[0]

        # pop from heap logn => n* (klogn) better than sorting if k is small
        # k = len(nums) - k
        # def quickSelect(l,r):
        #     p, pivot = l, nums[r]
        #     for i in range(l,r):
        #         if nums[i] <= pivot:
        #             nums[i], nums[p] =  nums[p], nums[i]
        #             p+=1
        #     nums[r], nums[p] =  nums[p], nums[r]

        #     if p<k: return quickSelect(p+1,r)
        #     elif p>k: return quickSelect(l,p-1)
        #     else: return nums[p]
        # return quickSelect(0,len(nums)-1)
        
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, right, mid = [],[],[]
            for num in nums:
                if num>pivot:
                    left.append(num)
                elif num<pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if len(left)>=k:
                return quickSelect(left, k)
            elif k>len(left)+len(mid):
                return quickSelect(right, k-len(left)-len(mid))
            else:
                return pivot
        return quickSelect(nums, k)
