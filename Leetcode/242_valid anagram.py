# anagram = a word formed by using different letters from a word & also using different letters only once 

# using sorted method (time complexity - o(nlogm + mlogn))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        
        return sorted(s) == sorted(t)
    
# using hash map (better solution , time complexity - o(n+m))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t) : 
            return False 

        countS , countT = {} , {}

        for i in range(len(s)) : 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS : 

            if countS[c] != countT.get(c,0) : 

                return False 

        return True 