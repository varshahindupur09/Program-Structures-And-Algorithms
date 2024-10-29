https://leetcode.com/problems/combination-sum/description/

#######################################################
SOLUTION 1: COMBINATION SUM
#######################################################
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def combinationSumHelper(candidates, current_index, current_sum, current_combination, target):
            if current_sum == target:
                answer.append(current_combination)
                return
            if current_sum > target:
                return
            for i in range(current_index, len(candidates)):
                combinationSumHelper(candidates, i, current_sum + candidates[i], current_combination + [candidates[i]], target ) 
        
        combinationSumHelper(candidates, 0, 0, [], target)
        return answer
