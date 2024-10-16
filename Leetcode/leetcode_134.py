# Greedy Algorithm
### It should be greedy alogorithmic approach. Key points to note - it has a unique solution, meaning we don't have to think of many possible ways to solve the problem.

###########################################################################
EXPLANATION
###########################################################################
While starting from any gas station the key point to understand is that if the car has gas at an afforfable cost then it will be able to move in circular way. 

The complexity is n^2.

The sum(gas) >= sum(cost). This would be because you can't travel the loop without gas and enough money.

###########################################################################
SOLUTION
###########################################################################

# O(n) time #O(1) space
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 # we won't be able to complete the circuit without enough gas and cost

        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            # print(total)
            if total < 0:
                total = 0
                start = i+1

        return start
            



        # getting the difference array
        # for i in range(len(gas)):
        # print(diff)

        return 1
 
        # for g in gas:
        #     total += g
            
            
        
        
