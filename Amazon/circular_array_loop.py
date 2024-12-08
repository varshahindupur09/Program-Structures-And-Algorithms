################################################################################
SOLUTION (https://leetcode.com/problems/circular-array-loop/)
################################################################################

# -1%6 == 5 (r = dividend - divisor.q) (r = (-1)-(6)*(-1))(r=5)
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited_index = set()

        def getNextIndex(index, curr_dir):
            next_index = (index + nums[index]) % n #1 #1
            if index == next_index:
                return -1

            next_dir = 1 if (nums[next_index]>0) else -1

            if (curr_dir != next_dir) or (index == next_index):
                return -1

            return next_index

        for i in range(n):
            sp, fp = i, i

            while True:
                visited_index.add(sp)
                visited_index.add(fp)

                curr_dir = 1 if (nums[i]>0) else -1
                # nums[0] = 2, so curr_dir = 1 (forward)
                # nums[0] = -1, so curr_dir = -1 (backward)

                sp = getNextIndex(sp, curr_dir)
                fp = getNextIndex(fp, curr_dir)

                if sp == -1 or fp == -1:
                    break

                fp = getNextIndex(fp, curr_dir)

                if sp == fp:
                    return True
        return False
