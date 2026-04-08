class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = collections.defaultdict(int)
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in dc:
                return [dc[diff],i]
            dc[nums[i]] = i
        