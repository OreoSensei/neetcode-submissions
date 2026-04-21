class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {target-nums[0]}
        for i in range(1, len(nums)):
            t = target - nums[i]
            if nums[i] in diff:
                output = [nums.index(t), i]
                return output
            diff.add(t)