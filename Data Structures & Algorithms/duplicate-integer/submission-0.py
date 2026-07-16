class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        op=set(nums)
        m=len(op)

        if n==m:
            return False
        else:
            return True