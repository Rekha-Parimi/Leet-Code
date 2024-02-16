class Solution(object):
    def moveZeroes(self, nums):
        k=0
        for char in nums:
            if(char!=0):
                nums[k]=char
                k+=1
        for j in range(k,len(nums)):
            nums[j]=0
        return nums