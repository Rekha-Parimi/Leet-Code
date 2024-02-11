class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        c=1
        for i in range(1,len(nums)):
            if(nums[i]==nums[k]):
                c+=1
            else:
                c=1
            if(c<=2):
                k+=1
                nums[k]=nums[i]
        return k+1