class Solution(object):
    def removeDuplicates(self, nums):
        def removeDuplicates(nums):
         if not nums:
          return 0

    # Initialize a pointer to keep track of unique elements
        unique_ptr = 0

    # Iterate through the array
        for i in range(1, len(nums)):
        # If the current element is different from the previous one
            if nums[i] != nums[unique_ptr]:
            # Move the unique_ptr forward
                unique_ptr += 1
            # Update the unique element at unique_ptr
                nums[unique_ptr] = nums[i]

    # Return the number of unique elements (length of the modified array)
        return unique_ptr + 1
