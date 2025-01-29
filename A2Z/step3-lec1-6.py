class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        last_ele = nums[n-k:]
        nums[n-k:] = nums[:n-k]
        nums[:n-k] = last_ele
