class Solution(object):
    def findDifference(self, nums1, nums2):
        l=[]
        k=[]
        j=[]
        for i in range(len(nums1)):
            if(nums1[i] not in nums2 and nums1[i] not in l):
                l.append(nums1[i])
        j.append(l)
        for i in range(len(nums2)):
            if(nums2[i] not in nums1 and nums2[i] not in k):
                k.append(nums2[i])
        j.append(k)
        return j
