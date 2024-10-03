# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        print("n ", n) 

        windowSize = sum(nums)
        print("windowSize ", windowSize)

        slideWindow = nums[:windowSize]
        print("slideWindow ", slideWindow)

        slide1s = sum(slideWindow)
        max1s = slide1s
        print("slide1s ", slide1s, "max1s ", max1s)

        for i in range(n):
            print("i ", i)
            if nums[(windowSize + i) % n] == 1:
                print("(windowSize + i) % n ", windowSize, i,  n)
                slide1s += 1  # Adding new one
                print(" if nums[(windowSize + i) % n] == 1: ", slide1s)

            if nums[i] == 1:
                slide1s -= 1  # Removing old one
                print("if nums[i] == 1: ", slide1s)

            max1s = max(max1s, slide1s)
            print("max1s ", max1s)

        print("windowSize - max1s ", windowSize - max1s)
        return windowSize - max1s  # Minimum swaps



        
