class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            m[target-nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in m and i != m[nums[i]]:
                if i < m[nums[i]]:
                    return [i, m[nums[i]]]
                else:
                    return [m[nums[i]], i]