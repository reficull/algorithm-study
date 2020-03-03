
class Solution:
    def rmNext(self,i, nums):
        if i+1 < len(nums) and nums[i] == nums[i+1]:
            del nums[i+1]
            i = i-1
        if i+1 >= len(nums):
            return len(nums)
        return self.rmNext(i+1, nums)

    def removeDuplicates(self, nums) -> int:

        count = len(nums)
        count = self.rmNext(0, nums)

        return count
