class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        count={}

        for i in range(n):
            counter= target-nums[i]
            if counter in count:
                return [count[counter],i]
            count[nums[i]]= count.get(nums[i],i)
