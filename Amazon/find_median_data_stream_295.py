############################################################################################################
REGULAR WAY (SORTING O(NLOGN))
############################################################################################################
class MedianFinder:

    def __init__(self):
        self.data_stream = []

    def addNum(self, num: int) -> None:
        self.data_stream.append(num)
        return None

    def findMedian(self) -> float:
        medianIndex = 0
        self.data_stream.sort()
        if len(self.data_stream) > 0:
            if len(self.data_stream) % 2 == 0: #even
                medianIndex = len(self.data_stream) // 2
                medianIndex -= 1
                median = float((self.data_stream[medianIndex] + self.data_stream[medianIndex + 1]) / 2)
                return median
            else: #odd
                medianIndex = len(self.data_stream) // 2
                median = float(self.data_stream[medianIndex])
                return median
        else:
            print("None")


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

############################################################################################################
IF SORTING COMES UP THEN USE HEAPQ
############################################################################################################

class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap -1,
        self.large = [] #minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # balance
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.small) + 1 < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

        return None

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        return ((-self.small[0] + self.large[0])/2.0)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


