class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # arrays are already sorted if we try to take the median that would be a redundant work
        # total = 3, halfboth = 1.5~1
        # get array 1's half
        # halfboth - array 1's half == array 2's half
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # running binary search on the smaller array
        if len(A) > len(B) :
            A, B = B, A
        
        l, r = 0 ,len(A) - 1

        while True:
            i = (l + r) // 2 #A #half of A
            j = half - i - 2 #B

            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            # if partition is correct?
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

