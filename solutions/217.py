"""
Contains Duplicate - LeetCode
sud0

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashmp = {}
        for i in nums:
            if i in hashmp:
                hashmp[i] += 1
                val = hashmp[i]
                if val >=2 :
                    return True
            else : 
                hashmp[i] = 1

        return False
        