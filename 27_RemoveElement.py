class Solution(object):
    def removeElement(self, nums, val):
        k=0
        for char in nums:
            if(char!=val):
                nums[k]=char
                k+=1
        print(nums)
        return k
            