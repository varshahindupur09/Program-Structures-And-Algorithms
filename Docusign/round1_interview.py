#!/bin/python3
import math
import os
import random
import re
import sys
from itertools import pairwise

# Custom Exception
class CustomException(Exception):    
    def __init__(self, message, payload=None):
        self.message = message
        self.payload = payload

    def __str__(self):
        return str(self.message)

# Function to find closest numbers
def minimumAbsDifference(arr):
    try:
        arr.sort()
        
        # Raise exception if array length is odd
        if len(arr) % 2 != 0:
            raise CustomException("Wrong array size", "Array size should be even")
        
        # Find minimum absolute difference between adjacent elements
        min_diff = min(b - a for a, b in pairwise(arr))
        
        # Return all pairs with that minimum difference
        return [[a, b] for a, b in pairwise(arr) if b - a == min_diff]
    
    except CustomException as e:
        print("CustomException occurred: {}".format(e))
        print("Details: {}".format(e.payload))
        return []

# Example usage
print("Valid input:", minimumAbsDifference([6, 2, 4, 10]))
print("Invalid input:", minimumAbsDifference([6, 2, 4, 10, 1]))


# Uncomment this block for manual input
"""
if __name__ == '__main__':
    numbers_count = int(input().strip())
    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = minimumAbsDifference(numbers)
    for pair in result:
        print(" ".join(map(str, pair)))
"""
