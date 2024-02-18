class Solution(object):
    def findMaxAverage(self, nums, k):
        s=sum(nums[:k])
        max_s= s
        for i in range(len(nums)-k):
            s= s-nums[i]
            s = s+nums[i+k]
            max_s = max(max_s,s)
        return max_s/float(k)