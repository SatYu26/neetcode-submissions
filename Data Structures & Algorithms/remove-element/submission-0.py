class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Edge case
        if len(nums) == 0:
            return 0
        
        # Start with two pointer
        i,j = 0, len(nums) - 1
        while(i<=j):
            # If both i'th and j'th element are equal to 'val', decrement j only.
            if nums[i] == val and nums[j] == val:
                j-=1
            # If only i'th element is equal to val, swap i'th with j'th elemnt, increment i
            # and decrement j
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            # If only j'th element = val, decrement j 
            elif nums[j] == val:
                j-=1
            # When both are not equal to val, increment only i
            else:
                i+=1

        return i