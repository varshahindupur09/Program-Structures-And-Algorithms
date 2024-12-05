########################################################################################
solution
########################################################################################
# # O(nlogn)
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexes = [(t[0],t[1], i) for i, t in enumerate(tasks)] 
        indexes.sort(key = lambda task: task[0])
        time = indexes[0][0]
        # print(indexes, time)
        output = []
        minheap = []
        i = 0

        while i < len(indexes) or minheap:
            while i < len(indexes) and time >= indexes[i][0]:
                heapq.heappush(minheap, [indexes[i][1], indexes[i][2]])
                i+=1
            if minheap:
                processing_time, index = heapq.heappop(minheap)
                time += processing_time
                output.append(index)
            else:
                time = indexes[i][0]

        return output

#######################################################################################
saving space 
########################################################################################
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
          t.append(i)
        tasks.sort(key = lambda task: task[0])
        time = tasks[0][0]
        output = []
        minheap = []
        i = 0

        while i < len(tasks) or minheap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minheap, [tasks[i][1], tasks[i][2]])
                i+=1
            if minheap:
                processing_time, index = heapq.heappop(minheap)
                time += processing_time
                output.append(index)
            else:
                time = tasks[i][0]

        return output


