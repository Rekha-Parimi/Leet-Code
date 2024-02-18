class Solution(object):
    def uniqueOccurrences(self, arr):
        l=[]
        k=list(set(arr))
        for i in range(len(k)):
            if(arr.count(k[i]) not in l):
                l.append(arr.count(k[i]))
            else:
                return False
        return True