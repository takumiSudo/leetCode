"""
242. Valid Anagram
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        s_mp = {}; t_mp = {}
        for i, j in zip(s, t):
            if i in s_mp:
                s_mp[i] += 1
            else : 
                s_mp[i] =1

            if j in t_mp:
                t_mp[j] += 1
            else : 
                t_mp[j] =1

        if s_mp == t_mp:
            return True
        else : 
            return False



"""
This can also be done with hashmaps
- At the end do a check if the mps are equal and if the maps are equal return True


## Problem : 


"""     