https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

######################################################################
SOLUTION 1: without left and right confusing pointers
######################################################################

# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashset - tracking the longest substring without repeating characters
        i,j,maxim = 0,0,0
        char_set = set()

        while j < len(s):
            if s[j] not in char_set:
                char_set.add(s[j])
                j += 1
                maxim = max(maxim, len(char_set))
                # print("1: ", char_set)
            else:
                char_set.remove(s[i])
                i += 1
                # print("2: ", char_set)
        return maxim


######################################################################
SOLUTION 2: with left and right confusing pointers
######################################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, maxlen = 0, 0
        charset = set()

        for right in range(n):
            if s[right] not in charset:
                charset.add(s[right])
                maxlen = max(maxlen, right - left + 1)
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])
        
        return maxlen

######################################################################
SOLUTION 3: with left and right and charset length
######################################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, maxlen = 0, 0
        charset = set()

        for right in range(n):
            if s[right] not in charset:
                charset.add(s[right])
                maxlen = max(maxlen, len(charset))
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])
        
        return maxlen
