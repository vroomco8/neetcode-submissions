class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for n in range(len(nums)):
            if (target - nums[n]) in seen:
                return [seen[target - nums[n]], n]
            seen[nums[n]] = n
        