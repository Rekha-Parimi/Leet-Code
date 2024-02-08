class Solution(object):
    def isSubsequence(self, s, t):
        sp=0
        if(len(s)==0):
            return True
        for char in t:
            if(s[sp]== char):
                sp+=1
                if(len(s)==sp):
                    return True
        return False
        