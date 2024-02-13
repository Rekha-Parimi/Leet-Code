class Solution(object):
    def mergeAlternately(self, word1, word2):
        if(len(word1)>=len(word2)):
            n=len(word2)
        else:
            n=len(word1)
        k=''
        for i in range(n):
            k+=word1[i]
            k+=word2[i]