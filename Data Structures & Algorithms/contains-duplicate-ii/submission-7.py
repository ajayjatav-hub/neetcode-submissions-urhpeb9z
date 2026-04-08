class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        while l < len(nums):
            r = l + 1
            while r < len(nums) and r <= l + k:
                if nums[l] == nums[r]:
                    return True
                r += 1
            l += 1
        return False