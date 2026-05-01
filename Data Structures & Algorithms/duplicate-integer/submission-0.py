class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set(nums)
        if len(nums) > len(arr):
            return True
        else:
            return False