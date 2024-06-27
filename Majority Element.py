class Solution:
    def majorityElement(self, nums) -> int:
        return max(Counter(nums).items(), key=lambda x: x[1])[0]