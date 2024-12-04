##########################################################################################
NOTE: O(1) < O(logn) < O(n) < O(nlogn)
##########################################################################################

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmapAnagrams = defaultdict(list)
        # hashmap is immutable therefore use tuple as key
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            hashmapAnagrams[key].append(s)

        return list(hashmapAnagrams.values())

    # O(n*m) = TC, SC = O(n*m)


##########################################################################################
VALID ANAGRAMS - BEST SOLUTION
##########################################################################################

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t


# O(n) is above solution

##########################################################################################
VALID ANAGRAMS - BAD 
##########################################################################################

 if used sorted then we get Nlogn ...

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted



